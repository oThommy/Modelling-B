#uses a text file to extract the flows and put them in the nodes' dictionary
def getflows(file):
    f = open(file,'r')
    line = f.readline()
    res = []
    while line:
        res.append([int(i) for i in line.split()])
        line = f.readline()
    f.close()
    return res
    
#uses a text file to extract the edges and put them in the nodes' dictionary
def getedges(file):
    f = open(file,'r')
    line = f.readline()
    res = []
    while line:
        res.append([int(i) for i in line.split()])
        line = f.readline()
    f.close()
    return res

#uses a text file to extract the edges and put them in the nodes' variable    
def getcosts(file):
    f = open(file,'r')
    res = f.read().split()
    f.close()
    return [int(i) for i in res]
    
def getmultipliers(file):
    f = open(file,'r')
    res = f.read().split()
    f.close()
    return [int(i) for i in res]

    
