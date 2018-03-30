# -*- coding: UTF-8 -*-
"""
sexualNetwork class.

Represent a network of sexual partners.
"""
import warnings
warnings.filterwarnings('ignore')
from Global_Value import *


class sexualNetwork(Graph):
    """This class gives a network of sexual partners.

    Nodes are people and edges are sexuals interactions
    """

    def __init__(self, n, m):
        """Initialize a sexual Network with the Barabasi-Albert method.

        n (int) is the number of individuals in the networkself.
        m (int) is the parameter for the Barabasi-Albert method.
        """
        self.__dict__ = nx.barabasi_albert_graph(n, m).__dict__.copy()
        self.Mydeg_rel = None
        self.MyD_rel = None
        self.Mycc_rel = None
        self.fitness = self.Update_Fitness()
        self.nbr_noeud = n

    def Mutation(self, proba):
        """Randomly mutate the nodes of the graph.

        When a nodes mutate, all its neighbours are changed unless they are of
        degree 1.
        proba (float) is the mutation probability.
        """
        nodes_to_mut = list(self.nodes)
        n = len(nodes_to_mut)
        for _ in range(n):
            nod_to_mut = rn.choice(nodes_to_mut)
            nodes_to_mut.remove(nod_to_mut)
            P = rn.uniform(0, 1)
            if (P < proba):
                # print(nod_to_mut)
                e = list(self.edges(nod_to_mut))
                rm = []
                for edge in e:
                    if (self.degree(edge[1]) == 1):
                        rm.append(edge)
                for e_to_rm in rm:
                    e.remove(e_to_rm)
                self.remove_edges_from(e)
                for j in range(len(e)):
                    partner = rn.choice(list(self.nodes))
                    self.add_edge(nod_to_mut, partner)

    def Mutation2(self, nb):
        #print("ooooooooooooooooooooooooooooo")
        #print("Debut mutation")
        #print(nx.is_connected(self))
        #print(self.edges())
        nodes_to_mut = rn.sample(list(self.nodes),nb)
        #print("nodes to mut : ")
        #print(nodes_to_mut)
        for i in nodes_to_mut:
            #print('----mut')
            #print(list(self.edges()))
            previous_partner = rn.choice(list(self.neighbors(i)))
            self.remove_edge(i, previous_partner)
            new_partner = rn.choice(list(self.nodes))
            while (new_partner in self.neighbors(i)) or (new_partner == i):
                #print("o")
                new_partner = rn.choice(list(self.nodes))
            self.add_edge(i,new_partner)
            #print(i)
            #print(previous_partner)
            #print(new_partner)
            if not(nx.is_connected(self)):
                #print("bad")
                self.remove_edge(i, new_partner)
                self.add_edge(i,previous_partner)
                #print(list(self.edges()))
        #print("Fin mutation")
        #print(nx.is_connected(self))
        #print(self.edges())
        #print("ooooooooooooooooooooooooooooo")
           

    def CrossOver(self, proba, n, graph_pop):
        """Do a Crossing Over with a random graph of a population.

        proba (float) is the probability of doing a crossing-over.
        n (int) is the number of nodes to cross between the graph.
        graph_pop ([graph]) is the population of graph from which a random
        graph is selected to do the crossing-over.
        """
        P = rn.uniform(0, 1)
        if (P < proba):
            graph = rn.choice(graph_pop)
            nodes_to_cross = rn.sample(list(self.nodes()), n)
            # print('oooooo')
            # print(nodes_to_cross)
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



    def CrossOver2(self, nb, graph_pop):
        """Do a Crossing Over (v2) with a random graph of a population.

        proba (float) is the probability of doing a crossing-over.
        n (int) is the number of nodes to cross between the graph.
        graph_pop ([graph]) is the population of graph from which a random
        graph is selected to do the crossing-over.
        """
        #print("ooooooooooooooooooooooooooooo")
        #print("Debut Cross")
        #print(nx.is_connected(self))
        #print(self.edges())
        #index = rn.randint(0, len(graph_pop)-1)
        #print("cross with : ", str(index))
        graph = rn.choice(graph_pop)
        #graph = graph_pop[index]
        #print("edges from other graph")
        #print(list(graph.edges()))
        init_BFS = rn.choice(list(graph.nodes()))
        nodes_to_cross = graph.limited_BFS(init_BFS,nb)
        #print("nodes_to_cross")
        #print(nodes_to_cross)
        e_to_rm = self.edges_between_nodes(nodes_to_cross)
        e_to_add = graph.edges_between_nodes(nodes_to_cross)
        #print("e_to_rm")
        #print(e_to_rm)
        self.remove_edges_from(e_to_rm)
        
        #print("e_to_add")
        #print(e_to_add)
        self.add_edges_from(e_to_add)
        #print('----------------------')
        #print("Fin Cross")
        #print(nx.is_connected(self))
        #if not(nx.is_connected(self)):
        #   z=input()
        #print(self.edges())
        #print("ooooooooooooooooooooooooooooo")

    def limited_BFS(self,init,n):
        queue = [init]
        res = [init]
        while len(res)<n and len(queue)>0:
            u = queue[0]
            near = list(self.neighbors(u))
            near = [x for x in near if x not in res]
            rn.shuffle(near)
            queue = queue + near
            res = res + near
            queue.remove(u)
        return(res[:n])

    def edges_between_nodes(self,nodes):
        edges = []
        for n in nodes:
            for vois in list(self.neighbors(n)):
                if vois in nodes:
                    edges.append((n,vois))
        return edges

    def Update_Fitness(self):
        """Update the fitness of the graph.

        This function compare the intrinseque parameters of the
        graph to the theorical parameters given by litterature (global_value)
        The fitness is calculated as a relativ difference between
        observed and theorical.
        """
        # Invariant d'echelle
        """ degrees distribution must follow a power law with 
        alpha as parameters """
        deg = self.Degree_distribution()
        deg_rel = (deg - alpha)**2/alpha
        self.Mydeg_rel =deg_rel
        try : 
            # Diametre
            D = nx.diameter(self)
            D_rel = (D - log(self.nbr_noeud))**2/log(self.nbr_noeud)
            self.MyD_rel=D_rel
            # Coefficient de clustering
            cc = self.node_clustering()
            if cc is None:
                self.fitness = None
                self.Mycc_rel=None
            else : 
                cc_rel = (cc-gama)**2/gama
                self.Mycc_rel=cc_rel
            # Fitness
                self.fitness = deg_rel + D_rel + cc_rel
        except : 
            self.fitness = None
            self.MyD_rel = None
            self.Mycc_rel = None

    def Degree_distribution(self):
        """Return the parameter of the power law of the degree distribution"""
        data_deg = dict(self.degree()).values()
        data_deg_val = list(data_deg)
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            # ton pl.fit
            fit = pl.Fit(data_deg_val, discrete=True)
        res = fit.power_law.alpha
        return(res)

    def node_clustering(self):
        """Return the parameter of the power law of clustering coeff distri."""
        coefficients_clustering_nodes = nx.clustering(self, nodes=None,
                                                      weight=None)
        coefficients = list(coefficients_clustering_nodes.values())
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            # ton pl.fit
            fit = pl.Fit(coefficients, discrete=True)
        F = fit.power_law.alpha
        if str(F) == 'nan':
            return(None)
        else:
            return(F)

    def Update_graph(self, proba_mutation, proba_crossing_over, graph_pop):
        """Make the graph evolve after its selection.

        The descendant of this graph has mutations with a probability
        of proba_mutation and make crossing over with a random graph of
        the given population with a probability proba_crossing_over
        """
        # Number of nodes for crossing over and mutation
        n_cross = rn.randint(1, self.nbr_noeud-1)
        n_mut = rn.randint(1, self.nbr_noeud-1)
        # Evolution
        P1 = rn.uniform(0, 1)
        if (P1 < proba_mutation):
            self.Mutation2(n_mut)
        P2 = rn.uniform(0, 1)
        if (P2 < proba_crossing_over):
            self.CrossOver2(n_cross, graph_pop)
        self.Update_Fitness()

    def DisplayGraph(self):
        """Plot a circular representation of the graph."""
        nx.draw_circular(self, with_labels=True, font_weight='bold')
        plt.show()


# Verifications
'''
G1 = sexualNetwork(15,1)

G2 = sexualNetwork(15,1)

plt.subplot(221)
nx.draw(G1, with_labels=True, font_weight='bold')

plt.subplot(222)
nx.draw(G2, with_labels=True, font_weight='bold')

G1.CrossOver2(5,G2)

plt.subplot(223)
nx.draw(G1, with_labels=True, font_weight='bold')

G2.CrossOver2(5,G1)

plt.subplot(224)
nx.draw(G2, with_labels=True, font_weight='bold')

plt.show()
'''

'''
A = sexualNetwork(15,1)
print(A.limited_BFS(10,6))
A.DisplayGraph()
'''

'''
G1 = sexualNetwork(20, 1)

G2 = sexualNetwork(20, 1)

plt.subplot(311)
nx.draw_circular(G1, with_labels=True, font_weight='bold')
plt.subplot(312)
nx.draw_circular(G2, with_labels=True, font_weight='bold')

G1.CrossOver2(1,5,G2)

plt.subplot(313)
nx.draw_circular(G1, with_labels=True, font_weight='bold')

plt.show()
'''

'''
G1 = sexualNetwork(15, 1)

plt.subplot(211)
nx.draw_circular(G1, with_labels=True, font_weight='bold')


G1.Mutation2(4)

plt.subplot(212)
nx.draw_circular(G1, with_labels=True, font_weight='bold')



plt.show()
'''


'''
G1 = sexualNetwork(40, 2)
Pop = [sexualNetwork(40, 2), sexualNetwork(40, 2), sexualNetwork(40, 2),
       sexualNetwork(40, 2), sexualNetwork(40, 2), sexualNetwork(40, 2)]
G1.Update_graph(mutation, crossing_over, Pop)
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
'''

