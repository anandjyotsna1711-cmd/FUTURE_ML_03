from pypdf import PdfReader
import io

def extract_text(file):
    filename = file.filename.lower()
    content = file.read()
    file.seek(0)

    if filename.endswith(".pdf"):
        reader = PdfReader(io.BytesIO(content))
        return "\n".join(
            page.extract_text() or "" for page in reader.pages
        )

    elif filename.endswith(".txt"):
        return content.decode("utf-8", errors="ignore")

    raise ValueError("Unsupported file format")