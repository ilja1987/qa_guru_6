import pytest
import zipfile
import os
import shutil


@pytest.fixture()
def arch():
    test_zip = zipfile.ZipFile('T_archive.zip', 'w')
    test_zip.write('test.pdf')
    test_zip.write('test.csv')
    test_zip.write('test.xls')
    test_zip.close()


@pytest.fixture()
def rem():
    yield
    os.remove('T_archive.zip')
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), './pdf')
    shutil.rmtree(path)
