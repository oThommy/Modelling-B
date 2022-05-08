# from dataclasses import dataclass
# from pprint import pprint
# from typing import Generic, TypeAlias, TypeVar
# import pandas as pd
# NodeId: TypeAlias = int
# Person = TypeVar('Person')

# class Person:
#     __name: str
#     __age: int

#     def __init__(self: Person, filepath: str) -> None:
#         self.__name = 'YEET'
#         self.__age = 20
    
#     @property
#     def name(self) -> str:
#         return self.__name

#     @property
#     def name(self) -> str:
#         return self.__name
    
#     @property
#     def name(self) -> str:
#         return self.__name
    
#     @property
#     def name(self) -> str:
#         return self.__name
    

# x = Person('file.json')
# pprint(x.name)

# from typing import Protocol, TypeVar
# T = TypeVar('T')
# U = TypeVar('U')
# class Series(Protocol['T', 'U']):
#     pass



# test3: Series[float, int]
# print(Series[float, int])


# df = pd.DataFrame(data=[[1,2], [3,4]])
# print(df)
# print(df.iloc[0])
# print(type(df))
# print(type(df.iloc[0]))

# class Test:
#     __slots__ = '__yeet', '__name', '__age'
#     __yeet: str

#     def __init__(self, yeet: str = 'YEET', name: str = 'Thom', age: int = 20) -> None:
#         self.__yeet = yeet
#         self.__name = name

#     @property
#     def yeet(self) -> str:
#         return self.__yeet
    
#     @property
#     def name(self) -> str:
#         return self.__name
    
#     # @property
#     # def age(self) -> int:
#     #     return self.__age
    
# x = Test()
# # print(x.age)
# from pathlib import Path
# from pprint import pprint
# from config import Config
# CONFIG = Config()
# pprint(CONFIG.GRAPHS_DIR_PATH)
from integer_linear_problem import ILP
x = ILP.from_excel('./lol.xlsx')
x.N
x.w
x.c

# testinggg: Path


import timeit
from numpy import int64
import pandas as pd

# x = pd.read_excel(r'.\..\brightspace-locker\Data assignment parcel transport 2 Large.xlsx', sheet_name='General information', header=None, index_col=0).squeeze('columns')
# print(x)
# print(x['transfer'])
# print(type(x))

f_ser = pd.read_excel(r'.\..\brightspace-locker\Data assignment parcel transport 2 Large.xlsx', sheet_name='f', index_col=0, header=None).squeeze('columns')
print(set(f_ser.index))

# x = pd.Series([1,2,3,4,5,6,7,8,9,10], dtype=int)
# def int_func():
#     x[0] * 10

# y = pd.Series([1,2,3,4,5,6,7,8,9,10], dtype=int64)
# def int64_func():
#     y[0] * 10

# N = 10000

# int_time = min(timeit.repeat(int_func, number=N))
# int64_time = min(timeit.repeat(int64_func, number=N))
# print(int_time)
# print(int64_time)
# print(f'improvement: {(int64_time - int_time) / int_time:.2%}')