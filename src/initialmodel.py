from pulp import *
from datasets_lists import *

def findHub(i,x,y):
    if value(y[i]) == 1:
        return i
    for j in range(nodes):
        if value(x[i][j]) == 1:
            return j
    return 0

#Input data
nodes = 10
costs = getcosts('smallcosts.txt') #list with length n 
c,t,d = getmultipliers('smallmultipliers.txt') #integers
flows = getflows('smallflows.txt') #nested list; n x n
edges = getedges('smalledges.txt') #nested list; n x n

#create LP problem
ParDe= LpProblem("ParDe", LpMinimize)

#introduce x variable
x = LpVariable.dicts("Connections",(range(nodes),range(nodes)),cat = LpBinary)

y = LpVariable.dicts('hubs',range(nodes),cat=LpBinary)

t1 = LpVariable.dicts('t1',(range(nodes),range(nodes)),cat = LpBinary)
t2 = LpVariable.dicts('t2',(range(nodes),range(nodes),range(nodes)),cat = LpBinary)
t3 = LpVariable.dicts('t3',(range(nodes),range(nodes),range(nodes),range(nodes)),cat=LpBinary)

#add objective function
ParDe += lpSum([costs[i] * y[i] for i in range(nodes)]) + lpSum([t1[i][j] * flows[i][j] * t * edges[i][j] for i in range(nodes) for j in range(nodes)]) + lpSum([t2[i][j][k] * (flows[i][j] * (c * edges[i][k] + t * edges[k][j]) + flows[j][i] * (t * edges[j][k] + d * edges[k][i])) for i in range(nodes) for j in range(nodes) for k in range(nodes)]) + lpSum([t3[i][j][k][l] * flows[i][j] * (c * edges[i][k] + t * edges[k][l] + d * edges[l][j]) for i in range(nodes) for j in range(nodes) for k in range(nodes) for l in range(nodes)])




#constraints




ParDe += lpSum([y[i] for i in range(nodes)]) >= 1

for i in range(nodes):
    ParDe += x[i][i]==y[i]

for i in range(nodes):
    for j in range(nodes):
        ParDe += x[i][j] >= t1[i][j]

for i in range(nodes):
    ParDe += lpSum([x[i][j] for j in range(nodes)]) <= 1 + (nodes-1) * y[i]
    ParDe += lpSum([x[i][j] for j in range(nodes)]) >= 1
    
for i in range(nodes):
    for j in range(nodes):
        ParDe += t1[i][j] <= y[i]
        ParDe += t1[i][j] <= y[j]
        ParDe += t1[i][j] >= y[i] + y[j] - 1

for i in range(nodes):
    for j in range(nodes):
        for k in range(nodes):
            ParDe += t2[i][j][k] <= 1 - y[i]
            ParDe += t2[i][j][k] <= y[j]
            ParDe += t2[i][j][k] <= x[i][j]
            ParDe += t2[i][j][k] >= 1 - y[i] + y[j] + x[i][j] - 2

for i in range(nodes):
    for j in range(nodes):
        for k in range(nodes):
            for l in range(nodes):
                ParDe += t3[i][j][k][l] <= 1 - y[i]
                ParDe += t3[i][j][k][l] <= 1 - y[j]
                ParDe += t3[i][j][k][l] <= x[i][k]
                ParDe += t3[i][j][k][l] <= x[l][j]
                ParDe += t3[i][j][k][l] >= 1 - y[i] + 1 - y[j] + x[i][k] + x[l][j] - 3

for i in range(nodes):
    for j in range(nodes):
        ParDe += y[i] + y[j] >= x[i][j]
        ParDe += x[i][j] == x[j][i]
    



#solve problem    
ParDe.solve()
    
#print status
print("Status:", LpStatus[ParDe.status])

#print objective function value
print("Total costs:", value(ParDe.objective))

        
for i in range(nodes):
    print([value(x[i][j]) for j in range(nodes)])
    print(value(y[i]))
    
