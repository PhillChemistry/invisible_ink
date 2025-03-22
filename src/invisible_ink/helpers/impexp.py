'''helper to manage importing of docx files and text files'''
from pathlib import Path

def import_txt(file_name: str) -> str:
    '''imports a text file based on its file name (including extensions!)'''
    file_path = Path(__file__).parents[3] / 'data' / file_name
    with open(file_path, 'r', encoding='utf-8'):
        try:
            text = file_path.read()
        except FileNotFoundError as e:
            print(f'no file at {file_path}')
            raise e
    return text
