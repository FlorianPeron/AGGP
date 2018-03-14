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
		self.nbr_noeud = n
	
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
		deg = Degree_distribution()
		deg_difference = 1-abs(1-deg/alpha)
		
		## Diametre 
		D = nx.diameter(self)
		D_difference = 1-abs(1-D/log(log(self.nbr_noeud)))
		
		## Coefficient de clustering
		cc = node_clustering()
		cc_difference = 1-abs(1-cc/gamma)
		
		## Fitness 
		self.fitness = 1/3 * deg_difference + 1/3 * D_difference + 1/3 * cc_différence
		
	def Degree_distribution(self) :
		#Obtaining list of degree values
		data_deg=dict(self.degree()).values()
		data_deg_val=list(data_deg)
		fit=pl.Fit(data_deg_val, discrete=True) 
		return(fit.power_law.alpha)

	def node_clustering(self):
		coefficients_clustering_nodes = nx.clustering(self, nodes=None, weight=None)
		coefficients = list(coefficients_clustering_nodes.values())
		fit = pl.Fit(coefficients, discrete = True)
		return(fit.power_law.alpha)
		
		



plt.subplot(211)
G1 = sexualNetwork(20,1)
nx.draw_circular(G1, with_labels=True, font_weight='bold')

nx.draw_circular(G, with_labels=True, font_weight='bold')

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
