#node class with the necessary variables
class Node:
    def __init__(self):
        self.isHub = False
        self.cost = 0
        self.edges = dict()
        self.flows = dict()
        
#graph to encapsulate all the nodes
class Graph:
    def __init__(self):
        self.nodes = list()
        self.collection = 0
        self.transfer = 0
        self.distribution = 0
    
    def add_node(self,node):
        self.nodes.append(node)
    
    def get_node(self,idx):
        return self.nodes[idx]

#uses a text file to extract the flows and put them in the nodes' dictionary
def getflows(file):
    f = open(file,'r')
    line = f.readline()
    counter = 0
    while line:
        c_info = [int(i) for i in line.split()]
        for i in range(len(c_info)):
            g.nodes[counter].flows[i] = c_info[i]
        counter += 1
        line = f.readline()
    f.close()
    
#uses a text file to extract the edges and put them in the nodes' dictionary
def getedges(file):
    f = open(file,'r')
    line = f.readline()
    counter = 0
    while line:
        c_info = [int(i) for i in line.split()]
        for i in range(len(c_info)):
            g.nodes[counter].edges[i] = c_info[i]
        counter += 1
        line = f.readline()
    f.close()

#uses a text file to extract the edges and put them in the nodes' variable    
def getcosts(file):
    f = open(file,'r')
    c_info = f.read().split()
    for i in range(len(c_info)):
        g.nodes[i].cost = int(c_info[i])
    f.close()
    
def getmultipliers(file):
    f = open(file,'r')
    c_info = f.read().split()
    g.collection = int(c_info[0])
    g.transfer = int(c_info[1])
    g.distribution = int(c_info[2])
    f.close()
    
#manually insert the amount of nodes in a given graph
number_of_nodes = 10
    
#create the graph with all the nodes
g = Graph()
for i in range(number_of_nodes):
    new_node = Node()
    g.add_node(new_node)

#add all the info to the graph
getflows('smallflows.txt')
getedges('smalledges.txt')
getcosts('smallcosts.txt')
getmultipliers('smallmultipliers.txt')
