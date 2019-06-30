import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import graphviz_layout

g=nx.Graph()

g.add_node(1)
g.add_node(2)


for i in range(1,5):
	g.add_node(i)

for i in range(4,1,-1):
	g.add_edge(i-1,i)
	if(i!=2):
		g.add_edge(i-2,i)
	if(i!=3):
		g.add_edge(i-3,i)

#g.add_edge(1,5)
#g.add_edge(2,3)
#g.add_edges_from([(1,2),(3,4)])
#nx.draw(g)
#plt.show()



#nx.draw(g, pos=graphviz_layout(g), node_size=1600, cmap=plt.cm.Blues, node_color=range(len(g)), prog='dot',with_labels=True)

nx.draw(g, os=graphviz_layout(g), node_size = 1200, node_color='skyblue',edge_color='red', width='3.0', with_labels = True)

plt.show()


