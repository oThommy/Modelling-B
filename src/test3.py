
# from typing import overload
# from multipledispatch import dispatch
# import pandas as pd
# from custom_typing import NodeId, Series, DataFrame

# @dispatch(dict[int, int])
# def to_pandas(*args: dict[NodeId, int]) -> Series[NodeId, int]:
#     print('series')
#     return pd.Series()

# @dispatch(dict[int, dict[int, int]])
# def to_pandas(*args: dict[NodeId, dict[NodeId, int]]) -> DataFrame[NodeId, Series[NodeId, int]]:
#     print('dataframe')
#     return pd.DataFrame()




# x: dict[int, dict[int, int]] = {
#     1: {
#         2: 100,
#         3: 400,
#     },
#     2: {
#         1: 200,
#         3: 500,
#     },
#     3: {
#         1: 483,
#         2: 492,
#     }
# }

# y = {
#     1: 200,
#     2: 400,
#     3: 500
# }

# to_pandas(y)
# to_pandas(x)

# print(pd.DataFrame.from_dict(x)[1][3])
# print('wreee')
# print(pd.DataFrame.from_dict(x))
# print(pd.Series(y))


# def test(*args):
#     return args

# print()
# x ,= test('hoi')
# print(x)
# print(type(x))

# from integer_linear_problem import ILP

# ilp = ILP.from_excel(r'./../brightspace-locker/Data assignment parcel transport 2 Small.xlsx')
# print(type(ilp.w.index))

    # @staticmethod
    # def dict_to_pandas(*dicts: dict) -> tuple[Series | DataFrame]:
    #     pass

class Test:
    __test: str = 'hoi'

    @property 
    def test(self) -> str:
        return self.__test

    def yeet(self):
        return self.test

lol = Test()
print(lol.yeet())