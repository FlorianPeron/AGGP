import networkx as nx
from networkx import Graph
from matplotlib import use
use('qt4agg')
import matplotlib.pyplot as plt
import random as rn
from Global_Value import *
import numpy as np
from math import *
import powerlaw as pl


class sexualNetwork(Graph):
	
	def __init__(self,n,m):
		self.__dict__ = nx.barabasi_albert_graph(n,m).__dict__.copy()
		self.fitness = self.Update_Fitness()
		self.nbr_noeud = n
	def Mutation(self,proba,n_mut_max):
		# Randomly mutate vertices
		# When a vertex mutate, its neighbours are changed (if their degree is bigger than one)
		for _ in range(n_mut_max):
			P = rn.uniform(0,1)
			if (P<proba):
				nod_to_mut = rn.choice(list(self.nodes))
				print(nod_to_mut)
				e = list(self.edges(nod_to_mut))
				rm = []
				for edge in e:
					if (self.degree(edge[1]) == 1):
						rm.append(edge)
				for e_to_rm in rm:
					e.remove(e_to_rm)
				self.remove_edges_from(e)
				for j in range(len(e)):
					partner = rn.choice(list(self.nodes))    # PB : the partner can be itself
					self.add_edge(nod_to_mut,partner)
					
	def CrossOver(self,proba,n,graph_pop):
		P = rn.uniform(0,1)
		if (P<proba):
			graph = rn.choice(graph_pop)
			nodes_to_cross = rn.sample(list(self.nodes()),n)
			print('ooooooooooooo')
			print(nodes_to_cross)
			for n in nodes_to_cross:
				e = list(self.edges(n))
				rm = []
				for edge in e:
					if (self.degree(edge[1]) == 1):
						rm.append(edge)
				for e_to_rm in rm:
					e.remove(e_to_rm)
				self.remove_edges_from(e)
			for n in nodes_to_cross:
				e = list(graph.edges(n))
				self.add_edges_from(e)
	
	
	def Update_Fitness(self) : 
		## Invariant d'echelle
		deg = self.Degree_distribution()
		deg_rel = (deg-alpha)**2/alpha
		
		## Diametre 
		D = nx.diameter(self)
		D_rel= (D - 1)**2/1

		## Coefficient de clustering
		cc = self.node_clustering()
		if cc == None : 
			self.fitness = None
		cc_rel = (cc-gama)**2/gama
		
		## Fitness 
		self.fitness = deg_rel + D_rel + cc_rel
		
		
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
	
	def DisplayGraph(self):
		nx.draw_circular(self, with_labels=True, font_weight='bold')
		plt.show()
		F = fit.power_law.alpha
		if str(F)  == 'nan' : 
			return(None)
		else : 
			return(F)
		
		

"""

G1 = sexualNetwork(40,1)
G1.DisplayGraph()



G1 = sexualNetwork(40,2)
G1.Fitness()
print(G1.fitness)
nx.draw(G1, with_labels=True, font_weight='bold')


plt.subplot(212)
G1.Mutation(0.3,10)
#print(G1.Fitness())
nx.draw(G1, with_labels=True, font_weight='bold')



plt.subplot(312)
G2 = sexualNetwork(20,1)
nx.draw_circular(G2, with_labels=True, font_weight='bold')

plt.subplot(313)
G2.CrossOver(1,3,G1)
nx.draw_circular(G2, with_labels=True, font_weight='bold')


plt.show()
"""
