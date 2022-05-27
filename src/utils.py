from dataclasses import dataclass, field, Field
from typing import Optional, TypeVar
from pathlib import Path
from tqdm import std
import datetime
import time
import os


T = TypeVar('T')

def ensure_dir_exists(dir_path: Path) -> None:
    '''ensures directory exists by creating the directory recursively if it doesn't exist yet'''
    
    if not dir_path.exists():
        os.makedirs(dir_path)

def count_dirs(dir_path: Path) -> int:
    '''returns amount of directories in dir_path (non-recursive)'''

    return len(next(os.walk(dir_path))[1])

def count_files(dir_path: Path) -> int:
    '''returns amount of files in dir_path (non-recursive)'''

    return len(next(os.walk(dir_path))[2])

def get_formatted_date(sep: str = '-', date: Optional[datetime.datetime] = datetime.datetime.now()) -> str:
    '''returns date string formatted with given seperator'''

    return date.strftime(sep.join(['%Y', '%m', '%d', '%H', '%M', '%S']))

def default_fact_field(obj: T, *args, **kwargs) -> Field:
    '''returns dataclass field with as default_factory the passed obj'''

    return field(*args, default_factory=lambda: obj, **kwargs)

def to_int(n: str | float | int) -> int:
    '''converts string, float or int to int'''

    return int(float(n))

def dict_dtypes_to_int(d: dict[T]) -> dict[T]:
    '''returns dictionary with keys and values converted to integers'''

    if isinstance(d, str | float | int):
        return to_int(d)

    ret_dict = dict()

    for key, val in d.items():
        ret_dict[to_int(key)] = dict_dtypes_to_int(val)
    
    return ret_dict

def complete_pbar(pbar: std.tqdm) -> None:
    '''set pbar to 100%'''

    pbar.n = 99
    pbar.update(1)

@dataclass(init=False, slots=True)
class Timer:
    '''stores execution time'''

    __start_time: float
    __end_time: float

    @property
    def total_time(self) -> str:
        seconds = self.__end_time - self.__start_time
        return str(datetime.timedelta(seconds=seconds))

    def start(self) -> None:
        '''start timer'''
        
        self.__start_time = time.perf_counter()

    def stop(self) -> None:
        '''stop timer'''

        self.__end_time = time.perf_counter()

    def __repr__(self) -> None:
        return f'Timer(total_time={self.total_time})'