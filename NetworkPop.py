from Global_Value import *
from Network import sexualNetwork

class NetworkPopulation():
	def __init__(self, pop_size, network_size):
		self.size = pop_size
		self.population = [sexualNetwork(network_size,2) for _ in range(self.size)]
		self.mutation = mutation
		self.crossing_over = crossing_over
		self.fitnessmean = []

	def Save_pop(self):
		for index in range(len(self.population)):
			with open("Population/essai"+str(index), 'wb') as f:
				nx.write_adjlist(pop.population[index],f)

	def Selection(self):
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
			return(np.random.choice(OtherPos,floor(self.size/2)+1-len(NonePos), p = np.array(weight)/sum(weight)))
			
	def Evolution(self) : 
		selected = self.Selection()
		for s in selected : 
			self.population[s].Update_graph(mutation,crossing_over,self.population)
	
	def EvoluNGeneration(self,n) : 
		for i in range (n):
			self.Evolution()
		


pop = NetworkPopulation(10,10)

pop.EvoluNGeneration(100)
plt.plot(pop.fitnessmean)
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
