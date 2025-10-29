import re
from collections import Counter
from PyPDF2 import PdfReader


def extract_text_from_pdf(pdf_file:str) -> list[str]:
    with open(pdf_file, 'rb') as pdf:
        reader = PdfReader(pdf, strict=False)



        print('Pages:', len(reader.pages))
        print('-' * 12) # Divider

        pdf_text: list[str] = [page.extract_text() for page in reader.pages]
        return pdf_text

def count_words(text_list: list[str]) -> Counter:
    


def main(): 
    extracted_text: list[str] = extract_text_from_pdf('sample.pdf')
    for page in extracted_text:
        print(page)





if __name__ == '__main__':
    main()