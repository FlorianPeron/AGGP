
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
			graph = self
			while graph == self :
				graph = rn.choice(graph_pop)
			nodes_to_cross = rn.sample(list(self.nodes()),n)
			for no in nodes_to_cross:
				e = list(self.edges(no))
				rm = []
				for edge in e:
					if (self.degree(edge[1]) == 1):
						rm.append(edge)
				for e_to_rm in rm:
					e.remove(e_to_rm)
				self.remove_edges_from(e)
			for no in nodes_to_cross:
				e = list(graph.edges(no))
				self.add_edges_from(e)
	
	
	def Update_Fitness(self) : 
		''' this function compare the intrinseque parameters of the 
		graph to the theorical parameters given by litterature (global_value)
		The fitness is calculated as a relativ difference between 
		observed and theorical '''
		
		## Invariant d'echelle
		deg = self.Degree_distribution()
		deg_rel = (deg-alpha)**2/alpha
		
		## Diametre 
		try : 
			D = nx.diameter(self)
		except : 
			D = None
			
		if D==None : 
			self.fitness = None
		else : 
			D_rel= (D - 1)**2/1

			## Coefficient de clustering
			cc = self.node_clustering()
			if cc == None : 
				self.fitness = None
			
			else : 
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
		'''This function makes the graph evolve after its selection. 
		The descendant of this graph has mutations with a probability 
		of proba_mutation and make crossing over with a random graph of
		the given population with a probability proba_crossing_over'''
		
		# Number of nodes for crossing over
		n_cross = rn.randint(0, self.nbr_noeud) 
		# Evolution
		self.Mutation(proba_mutation)
		self.CrossOver(proba_crossing_over, n_cross, graph_pop)
		self.Update_Fitness()
				
	def DisplayGraph(self):
		nx.draw_circular(self, with_labels=True, font_weight='bold')
		plt.show()




'''

G1 = sexualNetwork(40,2)
Pop = [sexualNetwork(40,2), sexualNetwork(40,2), sexualNetwork(40,2), sexualNetwork(40,2), sexualNetwork(40,2), sexualNetwork(40,2)]
G1.Update_graph(mutation, crossing_over, Pop)


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

'''
