"""Convert WAV audio files to MP3 format with volume adjustment.

This script processes WAV files from a source directory and converts them to MP3
format in a destination directory. It applies a volume boost of 1.5x during the
conversion.

The script:
- Looks for .wav files in ../papers/audio relative to the script location
- Converts them to .mp3 format using ffmpeg
- Saves the converted files to ~/Dropbox/NotebookLM/audio
- Only processes files that haven't already been converted
- Applies a 1.5x volume increase during conversion

Requirements:
    - ffmpeg must be installed and available in the system PATH
    - Source WAV files must be in a valid format supported by ffmpeg
"""

import os
import subprocess

base_dir = os.path.dirname(os.path.abspath(__file__))
source_dir = os.path.join(base_dir, "../papers/audio")
destination_dir = os.path.expanduser("~/Dropbox/NotebookLM/audio")

os.makedirs(destination_dir, exist_ok=True)

for file in os.listdir(source_dir):
    if file.endswith(".wav"):
        source_file = os.path.join(source_dir, file)
        destination_file = os.path.join(
            destination_dir, f"{os.path.splitext(file)[0]}.mp3"
        )
        if not os.path.isfile(destination_file):
            subprocess.run(
                [
                    "ffmpeg",
                    "-i",
                    source_file,
                    "-filter:a",
                    "volume=1.5",
                    destination_file,
                ],
                check=True,
            )
