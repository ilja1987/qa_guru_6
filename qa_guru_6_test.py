import zipfile
from PyPDF2 import PdfReader


def test_xlsx(arch):
    my_zip = zipfile.ZipFile('T_archive.zip', 'r')
    text = str(my_zip.read('test.xls'))
    assert text.__contains__('Call')


def test_csv():
    my_zip = zipfile.ZipFile('T_archive.zip', 'r')
    text = str(my_zip.read('test.csv'))
    assert text.__contains__('Unforgiven')


def test_pdf(rem):
    zipfile.ZipFile('T_archive.zip').extract('test.pdf', './pdf')
    reader = PdfReader('./pdf/test.pdf')
    page = reader.pages[0]
    assert page.extractText().__contains__('qa_guru')


