# from dataclasses import dataclass
# import inspect
# import json
# from pprint import pprint

# @dataclass
# class Test:
#     yeet: str = 'hoi'
#     hai: str = 'alsjf;laksjf'
#     hai1: str = 'sldkfjsd;alfkjs;dlkf'
#     hai2: str = 'oiwutoweputpqwtui'
#     hai3: str = 'nzmx.vnxz,.vmnzxc.,v'
#     yeet2: int = 24952094572094857
#     yeet3: int = 492710272243525
#     yeet34: int = 492710272243525
#     yeet35: int = 492710272243525
#     yeet35667: int = 492710272243525
#     yeet355: int = 492710272243525
#     __hoi: int = 424

#     @property
#     def YEEEEEEEEEEEEEEEEEEEET():
#         return 'hoi'

#     def to_json(self):
#         print(inspect.getmembers(self))

# # Test().to_json()
# print(Test().__dict__)




# from config import Config
# from integer_linear_problem import Ilp

# ilp = Ilp.from_excel(Config().DATA_SMALL_PATH)
# print(ilp)


import dill

from solution import Solution
with open(r'C:\Users\Thom van den Hil\Desktop\Modelling-B\src\out\intuitive_algo_1\8-Data assignment parcel transport 2 very small Small-2022-05-20-19-05-51\solution_8_Data assignment parcel transport 2 very small Small_2022_05_20_19_05_51.pickle', 'rb') as file:
    solution: Solution = dill.load(file)

print(solution)
print()
print()
print()
print()
print(solution.ilp.f)
print(solution.z)