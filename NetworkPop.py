from Global_Value import *
from Network import sexualNetwork


class NetworkPopulation():
	def __init__(self, pop_size, network_size):
		self.size = pop_size
		self.population = [sexualNetwork(network_size,1) for _ in range(self.size)]
		self.mutation = mutation
		self.crossing_over = crossing_over
		self.fitnessmean = []
		self.Subfitness = None
		self.SubfitnessMean = [[],[],[]]
		self.actualMinFitIndice = None
	def Save_pop(self):
		for index in range(len(self.population)):
			with open("Population\essai"+str(index), 'wb') as f:
				nx.write_adjlist(pop.population[index],f)

	def Save_best(self): 
		all_fitness = []
		GraphWithFitness = []
		for index in range(len(self.population)):
			if self.population[index].fitness != None:
				all_fitness.append(self.population[index].fitness)
				GraphWithFitness.append(self.population[index])
		index_min = all_fitness.index(min(all_fitness))
		with open("Best_graph1000", 'wb') as f:
			nx.write_adjlist(GraphWithFitness[index_min],f)


	def Selection(self,t):
		#return list of index of graph that will be selectionned for mutations
		weight = []
		NonePos = []
		OtherPos = []
		self.Subfitness = [[],[],[]]
		for index in range(self.size):
			fitness = self.population[index].fitness
			self.Subfitness[0].append(self.population[index].Mydeg_rel)
			self.Subfitness[1].append(self.population[index].MyD_rel)
			self.Subfitness[2].append(self.population[index].Mycc_rel)
			if fitness == None:
				NonePos.append(index)
			else : 
				OtherPos.append(index)
				weight.append(fitness)
		try : 
			self.fitnessmean.append(min(weight))
			self.actualMinFitIndice = weight.index(min(weight))
		except : 
			self.fitnessmean.append(None)
			self.actualMinFitIndice = None
		if len(NonePos)>= self.size/2:
			return(NonePos)
		else:
			weight_p = [w**(1+t/500) for w in weight]
			"""
			if (t%100==0):
				plt.subplot(211)
				plt.pie(weight)
				plt.subplot(212)
				plt.pie(weight_p)
				plt.show()
			"""
			ToReturn = list(np.random.choice(OtherPos,floor(self.size/2)+1-len(NonePos), p = np.array(weight_p)/sum(weight_p), replace = False))
			"""
			sortedIndex = np.argsort(np.array(weight))
			indicesToChange = sortedIndex[-floor(self.size/2)+1-len(NonePos):]
			ToReturn = [OtherPos[i] for i in indicesToChange]
			"""
			return(np.array(ToReturn + NonePos))
			
	def Evolution(self,t) : 
		selected = self.Selection(t)
		self.FilterSubFitness()
		for i in range(3):
			if self.actualMinFitIndice != None : 
				self.SubfitnessMean[i].append(self.Subfitness[i][self.actualMinFitIndice])
			else : 
				self.SubfitnessMean[i].append(None)
		for s in selected : 
			#print("|||||||||||||||||||| Le graph " + str(s) )
			self.population[s].Update_graph(mutation,crossing_over,self.population)
	
	def EvoluNGeneration(self,n) : 
		for i in range (n):
			#print([g.fitness for g in self.population])
			print("|||||||||||||||||||||||||||||||||||||||||||||||||||||| J'evolue",i)
			self.Evolution(i)
		
	def FilterSubFitness(self):
			ToDelete = []
			for i in range (3):
				for j in range (len(self.Subfitness[i])):
					if (self.Subfitness[i][j])==None or (self.Subfitness[i][j])=="nan":
						if not j in ToDelete : 
							ToDelete.append(j)
			ToDelete = sorted(ToDelete,reverse = True)
			for i in range(3):
				for j in range(len(ToDelete)):
					del self.Subfitness[i][ToDelete[j]]

pop = NetworkPopulation(100,1000)

nbrgen = 1000

pop.EvoluNGeneration(nbrgen)

"""
plt.plot(pop.fitnessmean)
plt.show()
"""
"""
fig = plt.figure()
plt.plot(pop.fitnessmean)
plt.savefig("myfig.png")
"""

pop.Save_best()

t = range(0,nbrgen,1)

#deg/D/cc
fig = plt.figure()
plt.plot(t,pop.SubfitnessMean[0],"r",t,pop.SubfitnessMean[1],"b",t,pop.SubfitnessMean[2],"g",t,pop.fitnessmean,"c--")
plt.savefig("Fitness1000.png")
plt.show()
"""
plt.subplot(311)
nx.draw_circular(pop.population[0], with_labels=True, font_weight='bold')

plt.subplot(312)
nx.draw_circular(pop.population[1], with_labels=True, font_weight='bold')

pop.population[0].CrossOver(1,5,pop.population)
plt.subplot(313)
nx.draw_circular(pop.population[0], with_labels=True, font_weight='bold')


plt.show()
"""
