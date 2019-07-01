import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import graphviz_layout


G=nx.path_graph(4)
cities = {0:"Toronto",1:"London",2:"Berlin",3:"New York"}

H=nx.relabel_nodes(G,cities)
 
print("Nodes of graph: ")
print(H.nodes())
print("Edges of graph: ")
print(H.edges())
nx.draw(H)
nx.draw(H, pos=graphviz_layout(H), node_size=1600, cmap=plt.cm.Reds,
        node_color=range(len(H)),
        prog='dot',with_labels=True)
plt.show()
#plt.savefig("path_graph_cities.png")
#plt.show()
