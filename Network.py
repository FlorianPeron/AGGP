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
	
	def Mutation(self,proba):
		for i in range(len(self.nodes)):
			P = rn.uniform(0,1)
			if (P<proba):
				print(i)
				e = list(self.edges(i))
				self.remove_edges_from(e)
				for j in range(len(e)):
					partner = rn.choice(list(self.nodes))
					self.add_edge(i,partner)
	
	def CrossOver(self,proba,n,graph):
		P = rn.uniform(0,1)
		if (P<proba):
			nodes_to_cross = rn.sample(list(self.nodes()),n)
			print(nodes_to_cross)
			for n in nodes_to_cross:
				e = list(self.edges(n))
				self.remove_edges_from(e)
			for n in nodes_to_cross:
				e = list(graph.edges(n))
				self.add_edges_from(e)
	
	def Fitness(self) : 
		## Invariant d'echelle
		## Petit monde
		## Coefficient de clustering
		self.fitness = 0
	
	

plt.subplot(211)
G1 = sexualNetwork(20,1)
nx.draw_circular(G1, with_labels=True, font_weight='bold')


plt.subplot(212)
G1.Mutation(0.1)
nx.draw_circular(G1, with_labels=True, font_weight='bold')

'''
plt.subplot(312)
G2 = sexualNetwork(20,1)
nx.draw_circular(G2, with_labels=True, font_weight='bold')

plt.subplot(313)
G2.CrossOver(1,3,G1)
nx.draw_circular(G2, with_labels=True, font_weight='bold')
'''

plt.show()
