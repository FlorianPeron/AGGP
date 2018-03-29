from Global_Value import *
from Network import sexualNetwork


class NetworkPopulation():
	def __init__(self, pop_size, network_size):
		self.size = pop_size
		self.population = [sexualNetwork(network_size,2) for _ in range(self.size)]
		self.mutation = mutation
		self.crossing_over = crossing_over
		self.fitnessmean = []
		self.Subfitness = None
		self.SubfitnessMean = [[],[],[]]
	def Save_pop(self):
		for index in range(len(self.population)):
			with open("Population/essai"+str(index), 'wb') as f:
				nx.write_adjlist(pop.population[index],f)

	def Selection(self):
		#return list of index of graph that will be selectionned for mutations
		weight = []
		NonePos = []
		OtherPos = []
		self.Subfitness = [[],[],[]]
		for index in range(self.size):
			fitness = self.population[index].fitness
			self.Subfitness[0].append(self.population[index].Mydeg_rel[-1])
			self.Subfitness[1].append(self.population[index].MyD_rel[-1])
			self.Subfitness[2].append(self.population[index].Mycc_rel[-1])
			if fitness == None:
				NonePos.append(index)
			else : 
				OtherPos.append(index)
				weight.append(fitness)
		try : 
			self.fitnessmean.append(np.min(np.array(weight)))
		except : 
			self.fitnessmean.append("nan")
		if len(NonePos)>= self.size/2:
			return(NonePos)
		else:
			weight = turn_to_power(weight,10)
			ToReturn = list(np.random.choice(OtherPos,floor(self.size/2)+1-len(NonePos), p = np.array(weight)/sum(weight), replace = False))
			"""
			sortedIndex = np.argsort(np.array(weight))
			indicesToChange = sortedIndex[-floor(self.size/2)+1-len(NonePos):]
			ToReturn = [OtherPos[i] for i in indicesToChange]
			"""
			return(np.array(ToReturn + NonePos))
			
	def Evolution(self) : 
		selected = self.Selection()
		self.FilterSubFitness()
		
		for i in range(3):
			self.SubfitnessMean[i].append(np.min(self.Subfitness[i]))
		for s in selected : 
			self.population[s].Update_graph(mutation,crossing_over,self.population)
	
	def EvoluNGeneration(self,n) : 
		for i in range (n):
			self.Evolution()
	
	def FilterSubFitness(self):
		ToDelete = [[],[],[]]
		for i in range (3):
			for j in range (len(self.Subfitness[i])):
				if (self.Subfitness[i][j])==None or (self.Subfitness[i][j])=="nan":
					ToDelete[i].append(j)
		for i in range (3):
			ToDelete[i] = sorted(ToDelete[i],reverse = True)
		for i in range(3):
			for j in range(len(ToDelete[i])):
				del self.Subfitness[i][ToDelete[i][j]]

pop = NetworkPopulation(20,20)

nbrGen = 500

pop.EvoluNGeneration(nbrGen)

"""
plt.plot(pop.fitnessmean)
plt.show()
"""
"""
fig = plt.figure()
plt.plot(pop.fitnessmean)
plt.savefig("myfig.png")
"""




print(pop.SubfitnessMean)
t = range(0,nbrGen,1)

#deg/D/cc
plt.plot(t,pop.SubfitnessMean[0],"r",t,pop.SubfitnessMean[1],"b",t,pop.SubfitnessMean[2],"g",t,pop.fitnessmean,"c--")
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
