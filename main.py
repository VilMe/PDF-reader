import re
from collections import Counter
from PyPDF2 import PdfReader


def extract_text_from_pdf(pdf_file:str) -> list[str]:
    with open(pdf_file, 'rb') as pdf:
        reader = PdfReader(pdf, strict=False)



        print('Pages:', len(reader.pages))
        print('-' * 10) # Divider

        pdf_text: list[str] = [page.extract_text() for page in reader.pages]
        return pdf_text

def main(): 
    extracted_text: list[str] = extract_text_from_pdf('sample.pdf')
    print(extracted_text)



if __name__ == '__main__':
    main()