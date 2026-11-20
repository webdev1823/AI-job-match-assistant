from io import BytesIO

from pypdf import PdfReader


def extract_pdf_text(data: bytes) -> str:
    """Return the text of a PDF (all pages). Raises ValueError if no text can be read."""
    reader = PdfReader(BytesIO(data))
    text = "\n".join((page.extract_text() or "") for page in reader.pages).strip()
    if not text:
        raise ValueError("No text found in this PDF (it may be a scanned image). Please paste the text instead.")
    return text
