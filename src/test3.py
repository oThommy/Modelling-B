# from config import Config
# import pickle
# import dill

# with open('TESTCONFIG.pickle', 'wb') as file:
#     dill.dump(Config(), file)

# print()

# import pulp as plp
# opt_model = plp.LpProblem(name="MIP Model")
import pulp as plp
# import random
# n = 10
# m = 5
# set_I = range(1, n+1)
# set_J = range(1, m+1)
# c = {(i,j): random.normalvariate(0,1) for i in set_I for j in set_J}
# a = {(i,j): random.normalvariate(0,5) for i in set_I for j in set_J}
# l = {(i,j): random.randint(0,10) for i in set_I for j in set_J}
# u = {(i,j): random.randint(10,20) for i in set_I for j in set_J}
# b = {j: random.randint(0,30) for j in set_J}


# opt_model = plp.LpProblem(name="MIP Model")

# # if x is Binary
# x_vars  = {(i,j):
# plp.LpVariable(cat=plp.LpBinary, name="x_{0}_{1}".format(i,j)) 
# for i in set_I for j in set_J}

# # >= constraints
# constraints = {j : opt_model.addConstraint(
# plp.LpConstraint(
#              e=plp.lpSum(a[i,j] * x_vars[i,j] for i in set_I),
#              sense=plp.LpConstraintGE,
#              rhs=b[j],
#              name="constraint_{0}".format(j)))
#        for j in set_J}

# objective = plp.lpSum(x_vars[i,j] * c[i,j] 
#                     for i in set_I 
#                     for j in set_J)

# opt_model.sense = plp.LpMinimize
# opt_model.setObjective(objective)

# opt_model.solve()
# plp.pulpTestAll()

from typing import TypedDict


class NameInfo(TypedDict):
    name: str
    first_letter: str


def get_info(name: str) -> NameInfo:
    return {'name': name, 'first_letter': name[0]}

print(get_info('hoi').name)