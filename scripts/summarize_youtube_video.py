import argparse
import logging
import os
import yt_dlp
import whisper
from litellm import completion, completion_cost

# Set your OpenAI API key
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

# Constants
MODEL_NAME = "gpt-4o"
WHISPER_MODEL_SIZE = "medium"
DEFAULT_AUDIO_PATH = "audio.mp3"
CONVERSION_RATE_USD_TO_TWD = 31.0  # Example exchange rate

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def download_audio(youtube_url, output_directory):
    """Download audio from YouTube and save as mp3."""
    logging.info(f"Downloading audio from {youtube_url}")
    audio_output_path = os.path.join(output_directory, "audio.mp3")

    ydl_options = {
        "format": "bestaudio/best",
        "outtmpl": audio_output_path.replace(".mp3", ""),
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ],
    }

    try:
        with yt_dlp.YoutubeDL(ydl_options) as ydl:
            ydl.download([youtube_url])
    except Exception as e:
        logging.error(f"Error downloading audio: {e}")
        raise

    logging.info(f"Downloaded audio to {audio_output_path}")
    return audio_output_path


def convert_audio(audio_input_path, output_directory):
    """Convert the downloaded audio file with ffmpeg."""
    converted_audio_path = os.path.join(output_directory, "audio_converted.mp3")
    command = f'ffmpeg -i "{audio_input_path}" -ar 16000 -ac 1 -map 0:a "{converted_audio_path}"'
    if os.system(command) != 0:
        raise RuntimeError(f"Failed to convert audio with command: {command}")
    logging.info(f"Converted audio saved to {converted_audio_path}")
    return converted_audio_path


def transcribe_audio(file_path):
    """Transcribe audio using Whisper API."""
    logging.info(f"Starting transcription for {file_path}")
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"Audio file not found: {file_path}")

    whisper_model = whisper.load_model(WHISPER_MODEL_SIZE)

    # Load and preprocess audio
    audio_data = whisper.load_audio(file_path)
    audio_data = whisper.pad_or_trim(audio_data)

    # Transcribe using local model
    transcription_result = whisper_model.transcribe(file_path, fp16=False)
    return transcription_result["text"]


def save_to_file(content, file_path):
    """Save content to a file."""
    try:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(content)
        logging.info(f"Content saved to {file_path}")
    except IOError as e:
        logging.error(f"Error saving to file {file_path}: {e}")
        raise


def read_from_file(file_path):
    """Read content from a file."""
    logging.info(f"Reading content from {file_path}")
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    except IOError as e:
        logging.error(f"Error reading from file {file_path}: {e}")
        raise


def create_summary(prompt):
    """Generate a summary using LiteLLM and convert cost from USD to TWD."""
    logging.info("Generating summary using LiteLLM")
    messages = [{"content": prompt, "role": "user"}]
    try:
        response = completion(model=MODEL_NAME, messages=messages)
        cost_usd = completion_cost(completion_response=response)
    except Exception as e:
        logging.error(f"Error generating summary: {e}")
        raise

    cost_twd = float(cost_usd) * CONVERSION_RATE_USD_TO_TWD
    logging.info(
        f"\033[91mResponse cost: ${float(cost_usd):.2f} USD ({cost_twd:.2f} TWD)\033[0m"
    )
    return response["choices"][0]["message"]["content"]


def fetch_video_title_and_date(youtube_url):
    """Get the YouTube video title and upload date."""
    ydl_options = {
        "quiet": True,
        "skip_download": True,
    }
    try:
        with yt_dlp.YoutubeDL(ydl_options) as ydl:
            info_dict = ydl.extract_info(youtube_url, download=False)
            title = info_dict.get("title", "output").replace("/", "_")
            upload_date = info_dict.get("upload_date", "unknown")
    except Exception as e:
        logging.error(f"Error fetching video info: {e}")
        raise
    return title, upload_date


def sanitize_string(input_string):
    """Sanitize a string by removing unwanted characters."""
    return "".join(
        char for char in input_string if char.isalnum() or char in (" ", "_")
    ).rstrip()


def handle_youtube_audio(youtube_url):
    """Main function to handle the workflow."""
    sanitized_url = youtube_url.replace("\\", "")
    logging.info(f"Processing YouTube audio for URL: {sanitized_url}")
    try:
        video_title, upload_date = fetch_video_title_and_date(sanitized_url)
    except Exception as e:
        logging.error(f"Failed to fetch video details: {e}")
        return

    sanitized_video_title = " ".join(sanitize_string(video_title).split())
    output_directory = os.path.join(
        os.getcwd(), f"{upload_date}_{sanitized_video_title}"
    )

    if os.path.exists(output_directory):
        logging.info(
            f"Output directory {output_directory} already exists. Skipping processing."
        )
        return

    os.makedirs(output_directory, exist_ok=True)
    logging.info(f"Created directory {output_directory}")

    try:
        audio_path = download_audio(sanitized_url, output_directory)
        converted_audio_path = convert_audio(audio_path, output_directory)

        transcript_file_path = os.path.join(output_directory, "transcript.txt")
        summary_file_path = os.path.join(output_directory, "summary.md")

        transcript = transcribe_audio(converted_audio_path)
        transcript_with_url = f"{transcript}\n\nSource URL: {sanitized_url}"
        save_to_file(transcript_with_url, transcript_file_path)

        summary = create_summary(
            (
                "The transcript is sourced from the YouTube video. "
                "Please focus on summarizing and organizing the key points and practical notes from the program, "
                "including any mentioned topics, strategies, methods, and insights.\n\n"
                "Transcript:\n\n"
                f"{transcript}"
            )
        )
        summary_with_url = f"{summary}\n\nSource URL: <{sanitized_url}>"
        save_to_file(summary_with_url, summary_file_path)

        # Remove audio files after all jobs are done
        for path in [audio_path, converted_audio_path]:
            if os.path.exists(path):
                os.remove(path)
                logging.info(f"Removed audio file {path}")

        if os.path.exists(summary_file_path):
            os.system(f'code "{summary_file_path}"')
    except Exception as e:
        logging.error(f"Error in processing YouTube audio: {e}")


def process_channel_videos():
    """Process a single YouTube video URL provided via command line."""
    parser = argparse.ArgumentParser(description="Process a YouTube video URL.")
    parser.add_argument(
        "youtube_url", type=str, help="The YouTube video URL to process."
    )
    args = parser.parse_args()

    handle_youtube_audio(args.youtube_url)


if __name__ == "__main__":
    process_channel_videos()