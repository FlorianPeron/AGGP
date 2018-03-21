import networkx as nx
from networkx import Graph
import powerlaw as pl

def testpldist(R,p):
    if R>0:
        return(True)
    else:
        return(False)

#Just for generating a Graph G
G = nx.Graph()
G.add_node(1)
#G.add_node(4)
G.add_nodes_from([2, 3])
G.add_edges_from([(1, 2), (1, 3)])

#Obtaining list of degree values
data_deg=dict(G.degree()).values()
data_deg_val=list(data_deg)
print("degree values",data_deg_val)

#Test if follow powerlaw distribution

#are we going to set a xmax value?
fit=pl.Fit(data_deg_val, discrete=True, xmin=1)
print(fit.power_law.alpha)

R,p=fit.distribution_compare('power_law','exponential',normalized_ratio=True)
print(R,p)

print(testpldist(R,p))
