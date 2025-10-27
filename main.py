import re
from collections import Counter
from PyPDF2 import PdfReader


def extract_text_from_pdf(pdf_file:str) -> list[str]:
    with open(pdf_file, 'rb') as pdf:
        reader = PdfReader(pdf, strict=False)



        print('Pages:', len(reader.pages))
        print('-' * 10) # Divider

        