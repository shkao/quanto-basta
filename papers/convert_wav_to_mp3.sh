#!/bin/bash
set -euo pipefail

for file in audio/*.wav; do
    if [[ -f "$file" ]]; then
        destination_dir=~/Dropbox/NotebookLM
        destination_file="$destination_dir/${file##*/%.wav}.mp3"
        mkdir -p "$destination_dir"
        if [[ ! -f "$destination_file" ]]; then
            ffmpeg -i "$file" -filter:a "volume=1.2" "$destination_file"
        fi
    fi
done
