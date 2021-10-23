import pdfplumber

with pdfplumber.open("pdf\GEWLNP01.01 (1).pdf") as pdf:
    first_page = pdf.pages[1]
    table = first_page.extract_table()
    print(table)
    # print(first_page)
    # print(first_page.char