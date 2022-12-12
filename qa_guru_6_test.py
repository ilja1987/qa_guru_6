import zipfile
import pytest

test_zip = zipfile.ZipFile('T_arhive.zip', 'w')
test_zip.write('test.pdf', compress_type=zipfile.ZIP_DEFLATED)
test_zip.write('test.csv', compress_type=zipfile.ZIP_DEFLATED)
test_zip.write('test.xls', compress_type=zipfile.ZIP_DEFLATED)
test_zip.close()


def test_xlsx():
    test_zip = zipfile.ZipFile('T_arhive.zip', 'r')
    text = str(test_zip.read('test.xls'))
    assert text.__contains__('Call')


def test_csv():
    test_zip = zipfile.ZipFile('T_arhive.zip', 'r')
    text = str(test_zip.read('test.csv'))
    assert text.__contains__('Unforgiven')



def test_pdf():
    test_zip = zipfile.ZipFile('T_arhive.zip', 'r')
    text = str(test_zip.read('test.pdf'))
    assert text.__contains__('Test PDF for qa_guru')
    print(text)