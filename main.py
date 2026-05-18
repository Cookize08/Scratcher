import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

path = r"YOU_PATH"
df = pd.read_csv(path)

central_user = "USERNAME"

G = nx.DiGraph()

G.add_node(central_user)

for username in df["Username"]:
    G.add_node(username)
    G.add_edge(central_user, username)

plt.figure(figsize=(14, 10))
pos = nx.spring_layout(G, k=1.2)

nx.draw_networkx_nodes(G, pos, node_size=500)
nx.draw_networkx_edges(G, pos, arrowstyle='-|>', arrowsize=15)
nx.draw_networkx_labels(G, pos, font_size=9)

plt.title("Grafo de usuários seguindo por vfrnca__500")
plt.axis('off')
plt.show()
