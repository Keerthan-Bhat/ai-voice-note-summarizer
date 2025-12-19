import whisper
import tempfile
import os
from audio_utils import convert_to_wav

model = whisper.load_model("base")

def transcribe_audio(uploaded_file):
    suffix = os.path.splitext(uploaded_file.name)[-1]

    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        tmp.write(uploaded_file.read())
        input_path = tmp.name

    wav_path = convert_to_wav(input_path)

    result = model.transcribe(wav_path)

    os.remove(input_path)
    os.remove(wav_path)

    return result["text"]
