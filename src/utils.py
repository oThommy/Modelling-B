from dataclasses import field, Field
from datetime import datetime
import os
from typing import Optional, TypeVar


T = TypeVar('T')

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

def get_formatted_date(sep: str = '-', date: Optional[datetime] = datetime.now()) -> str:
    '''returns date string formatted with given seperator'''

    return date.strftime(sep.join(['%Y', '%m', '%d', '%H', '%M', '%S']))

def default_fact_field(obj: T) -> Field:
    '''returns dataclass field with as default_factory the passed obj'''

    return field(default_factory=lambda: obj)