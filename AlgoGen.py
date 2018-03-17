from Global_Value import *
from Network import sexualNetwork


class NetworkPopulation():
	def __init__(self, pop_size, network_size):
		self.size = pop_size
		self.population = [sexualNetwork(network_size,2) for _ in range(self.size)]
		self.mutation = mutation
		self.crossing_over = crossing_over

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
			print("----",fitness)
			if fitness == None:
				NonePos.append(index)
			else :
				OtherPos.append(index)
				weight.append(fitness)
		if len(NonePos)>= self.size/2:
			return(NonePos)
		else:
			print("W",weight)
			print(NonePos)
			print(OtherPos)
			print(floor(self.size/2)+1-len(NonePos))
			print(np.array(weight)/sum(weight))
			return(np.random.choice(OtherPos,floor(self.size/2)+1-len(NonePos), p = np.array(weight)/sum(weight)))



pop = NetworkPopulation(2,10)


plt.subplot(311)
nx.draw_circular(pop.population[0], with_labels=True, font_weight='bold')

plt.subplot(312)
nx.draw_circular(pop.population[1], with_labels=True, font_weight='bold')

pop.population[0].CrossOver(1,5,pop.population)
plt.subplot(313)
nx.draw_circular(pop.population[0], with_labels=True, font_weight='bold')


plt.show()
