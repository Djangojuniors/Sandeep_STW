import pdfplumber
pdf_file = r"F:\Upwork\sandeep_upwork\pdf\Traditional 2.pdf"
tables=[]
with pdfplumber.open(pdf_file) as pdf:
    pages = pdf.pages
    for i,pg in enumerate(pages):
        tbl = pages[i].extract_tables()
        print(f'{i} --- {tbl}')