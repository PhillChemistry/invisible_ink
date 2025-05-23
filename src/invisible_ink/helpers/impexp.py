'''helper to manage importing of docx files and text files'''
from pathlib import Path
from docx import Document

def import_txt(file_name: str) -> str:
    '''imports a text file based on its file name (including extensions!)'''
    file_path = Path(__file__).parents[3] / 'data' / file_name
    with open(file_path, 'r', encoding='utf-8'):
        try:
            text = file_path.read_text()
        except FileNotFoundError as e:
            print(f'no file at {file_path}')
            raise e
    return text


def export_dox(file_name: str, document_obj: Document) -> None:
    '''write an object to a file file_name in the data direcotry'''
    file_path = Path(__file__).parents[3].resolve() / 'data' / file_name
    try:
        document_obj.save(file_path)
    except FileNotFoundError as e:
        print(f'could not find path {file_path}')
        raise e