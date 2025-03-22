'''test import export module'''
import os.path
from docx import Document
import invisible_ink.helpers.impexp as ie

TEST_TXT = 'mail_text.txt'
def test_import_text_returns_str():
    '''fn returns str'''
    assert isinstance(ie.import_txt(TEST_TXT), str)


def test_import_text_works_common_ex():
    '''test if the common examples works'''
    text = ie.import_txt(TEST_TXT)
    correct_txt = ('Greetings Mr. Moriarti,\n\nit is with great pleasure that'
    + ' I may inform you that the details of our deal')
    assert correct_txt in text


def test_export_file_common_use_case():
    '''tests that a docx file can be created'''
    docx_obj = Document()
    ie.export_dox('test.docx', docx_obj)
    docx_path = \
    r'C:\Users\Phill Chemie\Chemie\2_Coding\ipp\3_wartime_encryptions\invisible_ink\data\test.docx'
    assert os.path.isfile(docx_path)
