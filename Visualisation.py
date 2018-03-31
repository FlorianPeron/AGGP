import networkx as nx
import matplotlib.pyplot as plt
import sys

fichier = sys.argv[1]

G = nx.read_adjlist(fichier)

nx.draw_networkx(G,node_size=10, font_weight='normal', with_labels=False, style="dotted",node_color = 'b')
plt.show()
