import streamlit as st
from transcribe import transcribe_audio
from summarize import summarize_text

st.set_page_config(page_title="AI Voice Note Summarizer")
st.title("🎙️ AI Voice Note Summarizer")

audio_file = st.file_uploader(
    "Upload a voice note (mp3 / wav / m4a / mp4)",
    type=["mp3", "wav", "m4a", "mp4"]
)

# Initialize session state
if "transcript" not in st.session_state:
    st.session_state.transcript = None

if "summary_result" not in st.session_state:
    st.session_state.summary_result = None


if audio_file:
    st.audio(audio_file)

    # 🔹 Transcribe ONLY ONCE
    if st.session_state.transcript is None:
        with st.spinner("Transcribing audio..."):
            st.session_state.transcript = transcribe_audio(audio_file)

    st.subheader("📝 Transcript")
    st.text_area(
        "Transcript",
        st.session_state.transcript,
        height=250
    )

    # 🔹 Summarize WITHOUT re-transcribing
    if st.button("Generate Summary"):
        with st.spinner("Summarizing..."):
            st.session_state.summary_result = summarize_text(
                st.session_state.transcript
            )

    # 🔹 Display summary if available
    if st.session_state.summary_result:
        result = st.session_state.summary_result

        st.subheader("📌 Summary")
        st.write(result["summary"])

        st.subheader("🔑 Key Points")
        for p in result["key_points"]:
            st.write(f"- {p}")

        st.subheader("✅ Action Items")
        for a in result["action_items"]:
            st.write(f"- {a}")
