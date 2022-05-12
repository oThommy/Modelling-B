from datetime import datetime
import os


def remove_extension(base: str) -> str:
    '''returns basename without extension'''

    return os.path.splitext(base)[0]

def ensure_dir_exists(dir_path: str) -> None:
    '''ensures directory exists by creating the directory recursively if it doesn't exist yet'''
    
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

def count_dirs(dir_path: str) -> int:
    '''returns amount of directories in dir_path (non-recursive)'''

    return len(next(os.walk(dir_path))[1])

def get_date(sep: str = '-') -> str:
    '''returns date string with given seperator'''

    return f'{datetime.now():%Y-%m-%d-%H-%M-%S}'