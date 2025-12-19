import subprocess
import tempfile
import os

def convert_to_wav(input_path: str) -> str:
    """
    Converts any audio/video file to 16kHz mono WAV for Whisper.
    Returns path to the converted wav file.
    """
    wav_path = tempfile.mktemp(suffix=".wav")

    command = [
        "ffmpeg",
        "-y",
        "-i", input_path,
        "-ac", "1",          # mono
        "-ar", "16000",      # 16kHz
        wav_path
    ]

    subprocess.run(
        command,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    return wav_path
