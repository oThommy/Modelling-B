import inspect
import __main__
from io import StringIO
from pathlib import Path
from pprint import pprint
import webbrowser
from dataclasses import dataclass
import os
import __main__

import jsonpickle
from config import Config
# from config import Config
from integer_linear_problem import Ilp
import utils
from datetime import datetime
from solution import Solution
from time import time
import pickle
import dill

# print(Config().ROOT_DIR_PATH)
# print(Config().OUT_DIR_PATH)
# print(os.path.relpath(Config().OUT_DIR_PATH))
# os.makedirs('YEET', exist_ok=False)

# from datetime import datetime

# print(fr'5--{datetime.now():%Y-%m-%d-%H-%M-%S}')


# dir_path = os.path.realpath(os.path.join(Config().ROOT_DIR_PATH, 'yeet', 'hi'))
# print(dir_path)
# os.makedirs(dir_path)

# print(utils.get_date('_'))
# print(Config().GRAPH_OPTIONS)
# def timer_func(func):
#     # This function shows the execution time of 
#     # the function object passed
#     def wrap_func(*args, **kwargs):
#         t1 = time()
#         for _ in range(100):
#             result = func(*args, **kwargs)
#         t2 = time()
#         print(f'Function {func.__name__!r} executed in {(t2-t1):.4f}s')
#         return result
#     return wrap_func

# dir_path = r'C:\Users\Thom van den Hil\Desktop\Modelling-B'
# @timer_func
# def func1():
#     sum(os.path.isdir(os.path.join(dir_path, file)) for file in os.listdir(dir_path))

# @timer_func
# def func2():
#     sum(1 for _ in filter(os.path.isdir, os.listdir(dir_path)))

# @timer_func
# def func3():
#     len(next(os.walk(dir_path))[1])

# func1()
# func2()
# func3()


# sol.save()
# file_dir_path = Path(__file__).parent
# print(file_dir_path)
# path = Path(file_dir_path / 'yesdklfjsl').relative_to(file_dir_path)
# utils.ensure_dir_exists(Path(r'HOI'))
# inputfile_path = r'C:\Users\Thom van den Hil\Desktop\Modelling-B\src\in\Data assignment parcel transport 2 Small.xlsx'
# inputfile_path = r'Data assignment parcel transport 2 Small.xlsx'
# x = Path(inputfile_path).resolve().relative_to(Config().IN_DIR_PATH)
# print(x)

# sol = Solution(
#     493893,
#     {1,2,3}, 
#     {4,5,6},
#     {1: {2: 1, 3: 0}},
#     Ilp.from_excel(r'C:\Users\Thom van den Hil\Desktop\Modelling-B\src\in\Data assignment parcel transport 2 Small.xlsx'))
# print(sol.configRepr)
# print(sol.__module__)
# print(repr(sol))
# sol.save()

# sol.save()

# yeetfile = r'C:\Users\Thom van den Hil\Desktop\Modelling-B\src\out\test\7-Data assignment parcel transport 2 Small-2022-05-13-21-32-31\solution_7_Data assignment parcel transport 2 Small_2022_05_13_21_32_31.pickle'
# with open(yeetfile, 'rb') as file:
#     sol: Solution = dill.load(file)
# sol.print()
# Config = sol.config_class
# print(Config().OUT_DIR_PATH)



# from test3 import Greeting, greeting1, greeting2

# g = Greeting([greeting1, greeting2])
# with open('DELETE_TEST.pickle', 'wb') as file:
#     dill.dump(g, file)
# def greeting2():
#     return "YEEEEEEEEET!"
# # g = Greeting([greeting1, greeting2])
# with open('DELETE_TEST.pickle', 'rb') as file:
#     g = dill.load(file)
# print(type(g))
# g.greet()
# pprint(__main__)

import sys
# ilp = Ilp.from_excel(r'C:\Users\Thom van den Hil\Desktop\Modelling-B\src\in\Data assignment parcel transport 2 Small.xlsx')
# print(ilp)

# ilp = Ilp.from_excel(Config().DATA_MEDIUM_HUGE_PATH)
# pprint(ilp.to_dict()['N'])
# pprint(ilp.to_dict()['f'])
# pprint(ilp.to_dict()['w'][71])

