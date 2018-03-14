import networkx as nx
from networkx import Graph
from matplotlib import use
use('qt4agg')
import matplotlib.pyplot as plt
import random as rn
import Global_Value


class sexualNetwork(Graph):
	def __init__(self,n,m):
		self.__dict__ = nx.barabasi_albert_graph(n,m).__dict__.copy()
		self.fitness = 0
	
	def mutation(self,proba):
		for i in range(len(self.nodes)):
			P = rn.uniform(0,1)
			if (P<proba):
				print(i)
				e = list(self.edges(i))
				self.remove_edges_from(e)
				for j in range(len(e)):
					partner = rn.choice(list(self.nodes))
					self.add_edge(i,partner)
	
	def Fitness(self) : 
		## Invariant d'echelle
		## Petit monde
		## Coefficient de clustering
		self.fitness = 0
		

plt.subplot(211)
G = sexualNetwork(20,2)

nx.draw_circular(G, with_labels=True, font_weight='bold')

plt.subplot(212)
G.mutation(0.05)
nx.draw_circular(G, with_labels=True, font_weight='bold')

plt.show()
