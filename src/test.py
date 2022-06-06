from tkhtmlview import html_parser
import PySimpleGUI as sg
from pyvis.network import Network
import networkx as nx
import sys
import pandas as pd
import numpy as np
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
from graph_visualiser import visualise_graph
from config import Config
from integer_linear_problem import Ilp
import utils
from datetime import datetime
from solution import Solution
from time import sleep, time
import pickle
import dill
from custom_typing import version, Version, IlpSolverData
from enum import Flag, IntFlag, auto


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


# ilp = Ilp.from_excel(r'C:\Users\Thom van den Hil\Desktop\Modelling-B\src\in\Data assignment parcel transport 2 Small.xlsx')
# print(ilp)

# ilp = Ilp.from_excel(Config().DATA_MEDIUM_HUGE_PATH)
# pprint(ilp.to_dict()['N'])
# pprint(ilp.to_dict()['f'])
# pprint(ilp.to_dict()['w'][71])

# import time
# import datetime
# timer = utils.Timer()
# timer.start()
# time.sleep(2.45)
# timer.stop()
# print(timer.total_time)

# print(str(datetime.timedelta(seconds=3600 * 24 * 100 + 3600.34543985723952379)))
# print(5 or 'unkown')
# print(next(next(os.walk(r'C:\Users\Thom van den Hil\Desktop\Modelling-B\src\out\old-graphs'))))
# print(Path(__file__).stem)
# min_dataset_n = 10
# max_dataset_n = 11
# error_df = pd.DataFrame(
#     [[-0.829776, 0.0],
#     [-5, -2]], 
#     index=range(min_dataset_n, max_dataset_n + 1),
# )
# print(error_df)
# print(error_df.stack().describe())

# avg_error_ser = pd.Series(np.zeros((max_dataset_n - min_dataset_n + 1,)), index=range(min_dataset_n, max_dataset_n + 1))
# for index, row in error_df.iterrows():
#     avg_error_ser[index] = row.mean()
# print(avg_error_ser)
# print(avg_error_ser.describe())



def set_html(widget, html, strip=True):
    prev_state = widget.cget('state')
    widget.config(state=sg.tk.NORMAL)
    widget.delete('1.0', sg.tk.END)
    widget.tag_delete(widget.tag_names)
    html_parser.w_set_html(widget, html, strip=strip)
    widget.config(state=prev_state)

html = """
<td colspan="2" class="infobox-image"><a href="https://en.wikipedia.org/wiki/RoboCop" class="image">
<img alt="RoboCop (1987) theatrical poster.jpg" src="https://upload.wikimedia.org/wikipedia/en/thumb/1/16/RoboCop_%281987%29_theatrical_poster.jpg/220px-RoboCop_%281987%29_theatrical_poster.jpg" decoding="async" width="250" height="386" class="thumbborder" srcset="//upload.wikimedia.org/wikipedia/en/1/16/RoboCop_%281987%29_theatrical_poster.jpg 1.5x" data-file-width="248" data-file-height="374"></a>
<div class="infobox-caption" style="text-align:center">Directed by Paul Verhoeven<br>Release date July 17, 1987</div></td>
"""

font = ("Courier New", 12, 'bold')
sg.theme("DarkBlue3")
sg.set_options(font=font)

layout_advertise = [
    [sg.Multiline(
        size=(25, 10),
        border_width=2,
        text_color='white',
        background_color='green',
        disabled=True,
        no_scrollbar=True,
        expand_x=True,
        expand_y=True,
        key='Advertise')],
]

keypad = [
    ["Rad/Deg",          "x!",   "(",  ")", "%", "AC"],
    ["Inv",       "sin", "ln",   "7", "8", "9", "÷" ],
    ["Pi",        "cos", "log",  "4",  "5", "6", "x" ],
    ["e",         "tan", "√",    "1",  "2", "3", "-" ],
    ["Ans",       "EXP", "POW",  "0",  ".", "=", "+" ],
]

layout_calculator = [
    [sg.Button(
        key,
        size=(7, 4),
        expand_x=key=="Rad/Deg",
        button_color=('white', '#405373') if key in "1234567890" else sg.theme_button_color(),
     ) for key in line]
            for line in keypad]

layout = [
    [sg.Frame("Calculator", layout_calculator, expand_x=True, expand_y=True),
     sg.Frame("Advertise",  layout_advertise, expand_x=True, expand_y=True)],
]
window = sg.Window('Title', layout, finalize=True, use_default_focus=False)
for element in window.key_dict.values():
    element.block_focus()

advertise = window['Advertise'].Widget

html_parser = html_parser.HTMLTextParser()
set_html(advertise, html)
width, height = advertise.winfo_width(), advertise.winfo_height()

while True:

    event, values = window.read()
    if event in (sg.WINDOW_CLOSED, 'Exit'):
        break
    print(event, values)

window.close()