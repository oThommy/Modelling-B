from integer_linear_problem import ILP
FILEPATH = r'./../brightspace-locker/Data assignment parcel transport 2 Small.xlsx'
ilp = ILP(filepath=FILEPATH)

def get_z():
    pass

z_min = float('inf')

for _ in ilp.N:
    for current_hub in ilp.N:
        