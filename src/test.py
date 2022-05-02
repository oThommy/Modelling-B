from pyvis.network import Network
import networkx as nx
g = Network()

g.from_nx(nx.complete_graph(5))

g.show('test.html')