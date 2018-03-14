import networkx as nx
from networkx import Graph
from matplotlib import use
use('qt4agg')
import matplotlib.pyplot as plt


class sexualNetwork():
	def __init__(self,n,m):
		self.network = nx.barabasi_albert_graph(n,m)
		self.fitness = 0



G = sexualNetwork(10,2)

nx.draw(G.network, with_labels=True, font_weight='bold')

plt.show()
