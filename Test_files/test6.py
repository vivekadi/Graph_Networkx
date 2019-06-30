import networkx as nx
import pylab as plt
from networkx.drawing.nx_agraph import graphviz_layout, to_agraph
import pygraphviz as pgv

G = nx.DiGraph()
G.add_node("A",rank=0)
G.add_nodes_from(['B','C','D'],style='filled',fillcolor='red')
G.add_nodes_from(['D','F','G'])
G.add_nodes_from(['H'],label='target')
G.add_edge('A','B',arrowsize=2.0)
G.add_edge('A','C',penwidth=2.0)
G.add_edge('A','D')
G.add_edges_from([('B','E'),('B','F')],color='blue')
G.add_edges_from([('C','E'),('C','G')])
G.add_edges_from([('D','F'),('D','G')])
G.add_edges_from([('E','H'),('F','H'),('G','H')])

# set defaults
G.graph['graph']={'rankdir':'TD'}
G.graph['node']={'shape':'circle'}
G.graph['edges']={'arrowsize':'4.0'}

A = to_agraph(G)
print(A)
A.layout('dot')
A.draw('abcd.png')

nx.draw(G, pos=graphviz_layout(G), node_size=1600, cmap=plt.cm.Reds,
        node_color=range(len(G)),
        prog='dot', with_labels=True)
plt.show()