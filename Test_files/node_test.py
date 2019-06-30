import networkx as nx
import matplotlib.pyplot as plt

g=nx.Graph()

g.add_node(1)
g.add_node(2)


for i in range(1,5):
	g.add_node(i)

for i in range(5,1,-1):
	g.add_edge(i-1,i)
	if(i!=2):
		g.add_edge(i-2,i)
	if(i!=3):
		g.add_edge(i-3,i)

#g.add_edge(1,5)
#g.add_edge(2,3)
#g.add_edges_from([(1,2),(3,4)])


nx.draw(g)
plt.show()

