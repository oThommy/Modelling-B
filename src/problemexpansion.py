from pulp import *
from datasets_lists import *




# Input data
dc = 0.15
ntm_cost = 0
htm_cost = 0

ntm_lim = 1
htm_lim = 1

nodes = 10
costs = getcosts('smallcosts.txt') #list with length n 
c,t,d = getmultipliers('smallmultipliers.txt') #integers
flows = getflows('smallflows.txt') #nested list; n x n
edges = getedges('smalledges.txt') #nested list; n x n

# nodes = 15
# costs = getcosts('largecosts.txt') #list with length n 
# c,t,d = getmultipliers('largemultipliers.txt') #integers
# flows = getflows('largeflows.txt') #nested list; n x n
# edges = getedges('largeedges.txt') #nested list; n x n

#create LP problem
ParDe= LpProblem("ParDe", LpMinimize)

#introduce x variable


a = LpVariable.dicts('node_to_hub',(range(nodes),range(nodes)),cat = LpBinary)
P = LpVariable.dicts('paths',(range(nodes),range(nodes),range(nodes),range(nodes)),cat=LpBinary)

ntm = LpVariable.dicts('ntm',(range(nodes)),cat = LpBinary)
htm = LpVariable.dicts('htm',(range(nodes),range(nodes)),cat = LpBinary)

cntm1 = LpVariable.dicts('cntm1',(range(nodes),range(nodes),range(nodes),range(nodes)),cat=LpBinary)
cntm2 = LpVariable.dicts('cntm2',(range(nodes),range(nodes),range(nodes),range(nodes)),cat=LpBinary)

chtm = LpVariable.dicts('chtm',(range(nodes),range(nodes),range(nodes),range(nodes)),cat=LpBinary)



#add objective function

ParDe += lpSum([a[i][i] * costs[i] + ntm[i] * ntm_cost for i in range(nodes)])\
    + lpSum([htm[i][j] * htm_cost/2 for i in range(nodes) for j in range(nodes)])\
    + lpSum([P[i][k][l][j] * flows[i][j] * (c * edges[i][k] + t * edges[k][l] + d * edges[l][j])\
             - dc * flows[i][j] * ((cntm1[i][k][l][j] * c * edges[i][k]) + (cntm2[i][k][l][j] * d * edges[l][j]) + chtm[i][k][l][j] * t * edges[k][l])
             for i in range(nodes) for j in range(nodes) for k in range(nodes) for l in range(nodes)])

#constraints
ParDe += lpSum([a[i][i] for i in range(nodes)]) >= 1

for i in range(nodes):
    ParDe += lpSum([a[i][j] for j in range(nodes)]) == 1

for i in range(nodes):
    for j in range(nodes):
        ParDe += a[i][j] <= a[j][j]

for i in range(nodes):
    for j in range(nodes):
        for k in range(nodes):
            for l in range(nodes):
                ParDe += P[i][k][l][j] <= a[i][k]
                ParDe += P[i][k][l][j] <= a[j][l]
                ParDe += P[i][k][l][j] >= a[i][k] + a[j][l] - 1


for i in range(nodes):
    for j in range(nodes):
        for k in range(nodes):
            for l in range(nodes):
                ParDe += cntm1[i][k][l][j] <= ntm[k]
                ParDe += cntm1[i][k][l][j] <= P[i][k][l][j]
                ParDe += cntm1[i][k][l][j] >= ntm[k] + P[i][k][l][j] - 1
        
                ParDe += cntm2[i][k][l][j] <= ntm[l]
                ParDe += cntm2[i][k][l][j] <= P[i][k][l][j]
                ParDe += cntm2[i][k][l][j] >= ntm[l] + P[i][k][l][j] - 1
                
                ParDe += chtm[i][k][l][j] <= P[i][k][l][j]
                ParDe += chtm[i][k][l][j] <= htm[k][l]
                ParDe += chtm[i][k][l][j] >= P[i][k][l][j] + htm[k][l] - 1
                
                
for i in range(nodes):
    ParDe += ntm[i] <= a[i][i]
    
    
    
ParDe += lpSum([ntm[i] for i in range(nodes)]) <= ntm_lim
ParDe += lpSum([htm[i][j] for i in range(nodes) for j in range(nodes)]) <= 2 * htm_lim

for i in range(nodes):
    for j in range(nodes):
        ParDe += htm[i][j] == htm[j][i]
        ParDe += htm[i][j] <= a[i][i]
        ParDe += htm[i][j] <= a[j][j]

#solve problem    
ParDe.solve(GUROBI_CMD())
   
#print status
print("Status:", LpStatus[ParDe.status])

#print objective function value
print("Total costs:", int(value(ParDe.objective)), 'EUROOOOOS')

        
for i in range(nodes):
    print([int(value(a[i][j])) for j in range(nodes)])
    
print('\n\n')
print([int(value(a[i][i])) for i in range(nodes)],'\n')
for i in range(nodes):
    if value(a[i][i]) == 1:
        print(i,value(ntm[i]))

for i in range(nodes):
    for j in range(nodes):
        if value(a[i][i]) == value(a[j][j]) == 1 and i != j:
            print(i,j,value(htm[i][j]))
