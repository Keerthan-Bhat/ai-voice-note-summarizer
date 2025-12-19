🎙️ AI Voice Note Summarizer

An end-to-end AI-powered voice note summarization system that converts audio recordings into structured insights using speech recognition and a locally hosted large language model.

This project demonstrates real-world GenAI system design, including audio preprocessing, transcription, summarization, performance optimization, and robust error handling — all running locally and free of cost.

🚀 Features

🎧 Upload voice notes (mp3, wav, m4a, mp4)

🗣️ Automatic speech-to-text transcription using OpenAI Whisper

🧠 Structured summarization using a local LLM (Ollama)

📌 Generates:

Short summary

Key points

Action items (when applicable)

⚡ Optimized to avoid re-processing using session state

🛡️ Defensive JSON parsing to prevent crashes

🆓 Fully local, no paid APIs required

🧠 System Architecture
Audio / Video File
        ↓
FFmpeg (audio normalization)
        ↓
Whisper (speech → text)
        ↓
Local LLM via Ollama
        ↓
Structured JSON Output
        ↓
Streamlit UI

🛠️ Tech Stack

Python 3.10

Streamlit – UI & app framework

Whisper – Speech-to-text transcription

FFmpeg – Audio preprocessing

Ollama – Local LLM inference

Qwen2.5 (1.5B) – Fast, CPU-friendly summarization model

📂 Project Structure
ai-voice-note-summarizer/
│
├── app.py              # Streamlit application
├── transcribe.py       # Whisper transcription logic
├── summarize.py        # Local LLM summarization
├── audio_utils.py      # Audio preprocessing (FFmpeg)
├── requirements.txt
├── .gitignore
└── README.md

⚙️ Installation & Setup
1️⃣ Clone the repository
git clone https://github.com/<your-username>/ai-voice-note-summarizer.git
cd ai-voice-note-summarizer

2️⃣ Create virtual environment
python -m venv venv
venv\Scripts\activate   # Windows

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Install FFmpeg

Download from: https://www.gyan.dev/ffmpeg/builds/

Add ffmpeg/bin to system PATH

Verify:

ffmpeg -version

5️⃣ Install Ollama & model

Download Ollama: https://ollama.com/download

Pull the summarization model:

ollama pull qwen2.5:1.5b

▶️ Run the App
streamlit run app.py


Then:

Upload a voice note

Wait for transcription

Click Generate Summary

View structured insights instantly

🧪 Example Output

Summary

India overtakes China as the most populated country, highlighting demographic shifts and geographic diversity.

Key Points

India now has over 1.43 billion people

Population growth trends have shifted global rankings

Geography includes the Himalayas and major plains

Action Items

(Empty when content is informational, not task-oriented)

⚡ Performance Optimizations

Uses st.session_state to prevent re-transcription

Limits LLM context to avoid CPU hangs

Applies model-level token caps

Gracefully handles non-JSON LLM responses

🧠 Key Learnings

Handling long-form audio with local AI models

Managing Streamlit re-runs and state

Optimizing GenAI pipelines for CPU-only systems

Defensive parsing for unreliable LLM outputs

Real-world tradeoffs between cost, speed, and accuracy

🏆 Resume Highlight

Built an end-to-end AI voice note summarization system using Whisper for speech recognition and a locally hosted LLM, with optimized performance and robust error handling.

📌 Future Improvements

Speaker diarization

Timestamped summaries

PDF / Markdown export

Meeting vs lecture detection

Cloud deployment option

📄 License

This project is licensed under the MIT License.
