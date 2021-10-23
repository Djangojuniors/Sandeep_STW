import pdfminer.pdfdocument
import pdfplumber
import camelot
import tabula
from django.core.files.storage import default_storage
from django.conf import settings
import csv

import os



class BillExtraction:
    KEY_WORDS = ['Monthly', 'Quarterly', 'Half Yearly', 'Annually', 'Total', 'Half-Yearly'
                 'Accounts', 'Plan', 'Term', 'Sum Assured', 'Premium', 'Age', 'Sex', 'Gender']

    def __init__(self, file_name):
        self.pdf_name = file_name

    def table_data(self, csv_name):
        with open(csv_name, 'r') as file:
            reader = csv.reader(file)
            for i in reader:




    def is_bill(self, text):
        counter = 0
        for _ in self.KEY_WORDS:
            if _ in text:
                counter += 1
        return counter

    def pages(self):
        try:
            # with pdfplumber.open(default_storage.open(self.pdf_name)) as _pdf:
            with pdfplumber.open(self.pdf_name) as _pdf:
                return len(_pdf.pages)
        except pdfminer.pdfdocument.PDFEncryptionError:
            return 0

    def extract_all_text(self, page_number):
        # with pdfplumber.open(default_storage.open(self.pdf_name)) as _pdf:
        with pdfplumber.open(self.pdf_name) as _pdf:
            _page = _pdf.pages[page_number]
            _text = _page.extract_text()
            if _text is None: return ''
            else: return _text

    def extract_all_tables(self, page_number):
        # print(self.pdf_name)
        _pdf_name = self.pdf_name.split('/')[-1]
        # print(os.path.join(settings.MEDIA_ROOT, 'documents', _pdf_name), page_number)
        # _tables = tabula.read_pdf(os.path.join(settings.MEDIA_ROOT, 'documents', _pdf_name), pages=page_number, multiple_tables=True)
        _tables = tabula.read_pdf(self.pdf_name, pages=page_number, multiple_tables=True)
        if _tables[0].empty:
            # _tables = camelot.read_pdf(os.path.join(settings.MEDIA_ROOT, 'documents', _pdf_name), flavor='stream', edge_tol=10000, pages=str(page_number))
            _tables = camelot.read_pdf(self.pdf_name, flavor='stream', edge_tol=10000, pages=str(page_number))
            print(type(_tables))
            _tables = _tables[0].df
            print(type(_tables))
            _tables = [_tables, 0]
        print(type(_tables[0]))
        print('_tables')
        # print(_tables[0].empty)
        print('_tables')
        return _tables
        # _output_file = 'output' + os.sep + self.pdf_name.split('/')[-1].split('.')[0] + '.csv'
        # _tables.to_csv(_output_file)
