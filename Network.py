import networkx as nx
from networkx import Graph
from matplotlib import use
use('qt4agg')
import matplotlib.pyplot as plt
import random as rn

class sexualNetwork():
	def __init__(self,n,m):
		self.network = nx.barabasi_albert_graph(n,m)
		self.fitness = 0
	
	def mutation(self,proba):   # conserve le nombre d'edges dans le graph
		                        # effectue des mutations sur les edges
		for i in range(len(self.network.nodes)):
			P = rn.uniform(0,1)
			if (P<proba):
				print(i)
				e = list(self.network.edges(i))
				self.network.remove_edges_from(e)
				for j in range(len(e)):
					partner = rn.choice(list(self.network.nodes))
					self.network.add_edge(i,partner)
	

plt.subplot(211)
G = sexualNetwork(20,2)
nx.draw_circular(G.network, with_labels=True, font_weight='bold')


plt.subplot(212)
G.mutation(0.05)
nx.draw_circular(G.network, with_labels=True, font_weight='bold')

plt.show()
'''
plt.subplot(223)
G.mutation(0.05)
nx.draw(G.network, with_labels=True, font_weight='bold')


plt.subplot(224)
G.mutation(0.05)
nx.draw(G.network, with_labels=True, font_weight='bold')
plt.show()
'''
