
from Global_Value import *



class sexualNetwork(Graph):
	
	def __init__(self,n,m):
		self.__dict__ = nx.barabasi_albert_graph(n,m).__dict__.copy()
		self.fitness = self.Update_Fitness()
		self.nbr_noeud = n
	
	
	def Mutation(self,proba):
		# Randomly mutate vertices
		# When a vertex mutate, its neighbours are changed (if their degree is bigger than one)
		nodes_to_mut = list(self.nodes)
		n = len(nodes_to_mut)
		for _ in range(n):
			nod_to_mut = rn.choice(nodes_to_mut)
			nodes_to_mut.remove(nod_to_mut)
			P = rn.uniform(0,1)
			if (P<proba):

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
		F = fit.power_law.alpha
		if str(F)  == 'nan' : 
			return(None)
		else : 
			return(F)
		
	def Update_graph(self, proba_mutation, proba_crossing_over, graph_pop) : 
		n_cross = rn.randint(0, self.nbr_noeud)
		self.Mutation(proba_mutation)
		self.CrossOver(proba_crossing_over, n_cross, graph_pop)
		self.Update_Fitness()
				
	def DisplayGraph(self):
			nx.draw_circular(self, with_labels=True, font_weight='bold')
			plt.show()
			F = fit.power_law.alpha
			if str(F)  == 'nan' : 
				return(None)
			else : 
				return(F)
		
		




G1 = sexualNetwork(40,2)
G1.Fitness()
print(G1.fitness)
nx.draw(G1, with_labels=True, font_weight='bold')

'''
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

'''
plt.show()

