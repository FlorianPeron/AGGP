import networkx as nx
from networkx import Graph
from matplotlib import use
use('qt4agg')
import matplotlib.pyplot as plt
import Global_Value
import numpy as np
from math import log
import powerlaw as pl


class sexualNetwork():
	def __init__(self,n,m):
		self.nbr_noeud = n
		self.network = nx.barabasi_albert_graph(n,m)
		self.fitness = 0
	
	
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
		
		### Fitness
	


	def node_clustering(self):
		coefficients_clustering_nodes = nx.clustering(self.network, nodes=None, weight=None)
		coefficients = list(coefficients_clustering_nodes.values())
		fit = pl.Fit(coefficients, discrete = True)
		return(fit.power_law.alpha)


G = sexualNetwork(1000,2)
print(G.node_clustering())
#nx.draw(G.network, with_labels=True, font_weight='bold')
G.Fitness()
plt.show()
