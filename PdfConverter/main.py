from pdf2docx import Converter

pdf_file = input("Pdfin adresini eksiksiz giriniz: ")
docx_file = "WordDosyası.docx"

cv = Converter(pdf_file)
cv.convert(docx_file)
cv.close()