from Global_Value import *
from Network import sexualNetwork

class NetworkPopulation():
	def __init__(self, pop_size, network_size):
		self.population = [sexualNetwork(network_size,1) for _ in range(pop_size)]


pop = NetworkPopulation(3,10)

plt.subplot(311)
nx.draw_circular(pop.population[0], with_labels=True, font_weight='bold')

plt.subplot(312)
nx.draw_circular(pop.population[1], with_labels=True, font_weight='bold')

pop.population[0].CrossOver(1,5,pop.population[1])
plt.subplot(313)
nx.draw_circular(pop.population[0], with_labels=True, font_weight='bold')


plt.show()
