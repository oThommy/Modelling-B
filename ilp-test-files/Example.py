# -*- coding: utf-8 -*-
"""
Created on Tue May 14 14:33:24 2019

@author: theresiavaness
"""
from pulp import *

#Input data
plants=3
cities=4
supply=[40,50,40]
demand=[45,20,30,30]
costs=[[8,6,10,9],[9,12,13,7],[14,9,16,5]]

#create LP problem
Powerco= LpProblem("Powerco", LpMinimize)

#introduce x variable
x = LpVariable.dicts("electricity",(range(plants),range(cities)),0,None)

#add objective function
Powerco += lpSum([costs[i][j]*x[i][j] for i in range(plants) for j in range(cities)]), "Total costs"

#constraint supply
for i in range(plants):
    Powerco += lpSum([x[i][j] for j in range(cities)])<=supply[i]
    
#constraint demand
for j in range(cities):
    Powerco += lpSum([x[i][j] for i in range(plants)])==demand[j]
 
#solve problem    
# Powerco.solve(GUROBI_CMD())
Powerco.solve(CPLEX_CMD())
# Powerco.solve()
    
#print status
print("Status:", LpStatus[Powerco.status])

#print objective function value
print("Total costs:", value(Powerco.objective))

#print solution
for i in range(plants):
    for j in range(cities):
        if value(x[i][j])>0:
            print(i,j,value(x[i][j]))
        
