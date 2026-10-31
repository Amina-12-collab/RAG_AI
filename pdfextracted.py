import fitz
pdf = fitz.open("documents/PYTHON FULL NOTES.pdf")
for page_number, page in enumerate(pdf, start=1):
    extracted_text = page.get_text()
    print("\nPage:", page_number)
    print(extracted_text)
pdf.close()