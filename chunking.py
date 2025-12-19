def chunk_text(text, max_words=300, overlap=50):
    words = text.split()
    chunks = []

    start = 0
    while start < len(words):
        end = start + max_words
        chunk = words[start:end]
        chunks.append(" ".join(chunk))
        start = end - overlap  # overlap for context

    return chunks