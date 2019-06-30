import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import graphviz_layout
from networkx.algorithms import node_classification


G = nx.path_graph(4)
G.edges()

G.node[0]['label'] = 'A'
G.node[3]['label'] = 'B'
node_classification.harmonic_function(G)  # doctest: +SKIP

nx.draw(G, pos=graphviz_layout(G), node_size=1600, cmap=plt.cm.Reds,
        node_color=range(len(G)),
        prog='dot',with_labels=True)
plt.show()