from PyPDF2 import PdfReader


class PDF:
    def __init__(self, pdf_file="example.pdf"):
        self.pdf_file = PdfReader(pdf_file)
        self.pages = self.pdf_file.pages

    def get_text(self):
        text = ""
        for page in self.pages:
            text += page.extract_text()
        text.replace('\n', '')
        return text
