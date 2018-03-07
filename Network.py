import networkx as nx
from networkx import Graph


class sexualNetwork(Graph):
    def __init__(self,n,m):
        self = nx.barabasi_albert_graph(n,m)


