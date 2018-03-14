import networkx as nx
from networkx import Graph
from matplotlib import use
use('qt4agg')
import matplotlib.pyplot as plt
import random as rn
import Global_Value
import numpy as np
from math import log
import powerlaw as pl


class sexualNetwork(Graph):
	def __init__(self,n,m):
		self.__dict__ = nx.barabasi_albert_graph(n,m).__dict__.copy()
		self.fitness = 0
		self.nbr_noeud
	
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
		deg = self.network.degree()
		print(deg)
		## Diametre 
		D = nx.diameter(self.network)
		D_difference = 1-abs(1-D/log(log(self.nbr_noeud)))
		
		## Coefficient de clustering
		cc = node_clustering()
		cc_difference = 1-abs(1-cc/gamma)
		


	def node_clustering(self):
		coefficients_clustering_nodes = nx.clustering(self.network, nodes=None, weight=None)
		coefficients = list(coefficients_clustering_nodes.values())
		fit = pl.Fit(coefficients, discrete = True)
		return(fit.power_law.alpha)
G = sexualNetwork(10,2)

nx.draw_circular(G, with_labels=True, font_weight='bold')

plt.subplot(212)
G.mutation(0.05)
nx.draw_circular(G, with_labels=True, font_weight='bold')

plt.show()
