import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

path = r"C:\Users\vinic\OneDrive\Área de Trabalho\Novo projeto\Faculdade\instagram-grafo\IGFollow_vfrnca__500_followers.csv"
df = pd.read_csv(path)

central_user = "vfrnca_"

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
