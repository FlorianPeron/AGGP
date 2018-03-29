from Global_Value import *
from Network import sexualNetwork


class NetworkPopulation():
	def __init__(self, pop_size, network_size):
		self.size = pop_size
		self.population = [sexualNetwork(network_size,1) for _ in range(self.size)]
		self.mutation = mutation
		self.crossing_over = crossing_over
		self.fitnessmean = []

	def Save_pop(self):
		for index in range(len(self.population)):
			with open("Population/essai"+str(index), 'wb') as f:
				nx.write_adjlist(pop.population[index],f)

	def Save_best(self): 
		all_fitness = []
		for index in range(len(self.population)):
			all_fitness.append(self.population[index].fitness)
		index_min = all_fitness.index(min(all_fitness))
		with open("Population/Best_graph", 'wb') as f:
			nx.write_adjlist(pop.population[index_min],f)


	def Selection(self,t):
		#return list of index of graph that will be selectionned for mutations
		
		weight = []
		NonePos = []
		OtherPos = []
		for index in range(self.size):
			fitness = self.population[index].fitness
			if fitness == None:
				NonePos.append(index)
			else : 
				OtherPos.append(index)
				weight.append(fitness)
		try : 
			self.fitnessmean.append(np.array(weight).min())
		except : 
			self.fitnessmean.append("nan")
		if len(NonePos)>= self.size/2:
			return(NonePos)
		else:
			weight_p = [w**(1+t/500) for w in weight]
			'''
			if (t%100==0):
				plt.subplot(211)
				plt.pie(weight)
				plt.subplot(212)
				plt.pie(weight_p)
				plt.show()
			'''
			ToReturn = list(np.random.choice(OtherPos,floor(self.size/2)+1-len(NonePos), p = np.array(weight_p)/sum(weight_p), replace = False))
			'''
			sortedIndex = np.argsort(np.array(weight))
			indicesToChange = sortedIndex[-floor(self.size/2)+1-len(NonePos):]
			ToReturn = [OtherPos[i] for i in indicesToChange]
			'''
			return(np.array(ToReturn + NonePos))
			
	def Evolution(self,t) : 
		selected = self.Selection(t)
		for s in selected : 
			self.population[s].Update_graph(mutation,crossing_over,self.population)
	
	def EvoluNGeneration(self,n) : 
		for i in range (n):
			#print([g.fitness for g in self.population])
			self.Evolution(i)
		


pop = NetworkPopulation(50,20)

pop.EvoluNGeneration(1000)
#pop.Save_best()
print(pop.fitnessmean[1:])
plt.plot(pop.fitnessmean[1:])
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
