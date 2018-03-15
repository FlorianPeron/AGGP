from Global_Value import *
from Network import sexualNetwork

class NetworkPopulation():
	def __init__(self, pop_size, network_size):
		self.size = pop_size
		self.population = [sexualNetwork(network_size,2) for _ in range(self.size)]
		self.fitess = np.array([0 for _ in range(self.size)])

	def Save_pop(self):
		for index in range(len(self.population)):
			with open("Population/essai"+str(index), 'wb') as f:
				nx.write_adjlist(pop.population[index],f)

	def Update_fitness(self):
		for index in range(self.size):
			self.fitness[index] = self.population[index].Fitness()
			self.fitness = self.fitness / np.sum(self.fitness)


pop = NetworkPopulation(20,10)

t = 0

while



plt.subplot(311)
nx.draw_circular(pop.population[0], with_labels=True, font_weight='bold')

plt.subplot(312)
nx.draw_circular(pop.population[1], with_labels=True, font_weight='bold')

pop.population[0].CrossOver(1,5,pop.population)
plt.subplot(313)
nx.draw_circular(pop.population[0], with_labels=True, font_weight='bold')


plt.show()
