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
