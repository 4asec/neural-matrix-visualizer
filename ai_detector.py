import torch
import torch.nn as nn
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

# 1. Setup Device GPU
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"🧠 Memulai AI pada perangkat: {device}")

# 2. Arsitektur Jaring-Jaring Rapi (4 -> 12 -> 6 -> 1)
class PremiumNeuralNetwork(nn.Module):
    def __init__(self):
        super(PremiumNeuralNetwork, self).__init__()
        self.layer1 = nn.Linear(4, 12)
        self.layer2 = nn.Linear(12, 6)
        self.output = nn.Linear(6, 1)

    def forward(self, x):
        return x

# 3. GENERATOR ANIMASI 
def buat_animasi ():
    G = nx.DiGraph()
    layers = [4, 12, 6, 1] # Formasi supaya rapi
    pos = {}
    
    node_id = 0
    layer_nodes = {}
    for layer_idx, num_nodes in enumerate(layers):
        layer_nodes[layer_idx] = []
        for n in range(num_nodes):
            G.add_node(node_id)
            pos[node_id] = (layer_idx, n - num_nodes / 2)
            layer_nodes[layer_idx].append(node_id)
            node_id += 1

    for l in range(len(layers) - 1):
        for s in layer_nodes[l]:
            for d in layer_nodes[l+1]:
                G.add_edge(s, d)

    fig, ax = plt.subplots(figsize=(10, 6))

    def update(frame):
        ax.clear()
        ax.set_title("Neural Network Connection Concept", fontsize=13, fontweight='bold', color='#64748b')
        fig.patch.set_facecolor('#090d16') # Latar Belakang Hitam Cyber Premium
        ax.set_facecolor('#090d16')
        
        # Logika kedip acak 
        node_colors = []
        for i in range(len(G.nodes)):
            if random.random() > 0.4:
                node_colors.append(random.choice(['#38bdf8', '#4ade80'])) # Biru / Hijau Menyala
            else:
                node_colors.append('#1e293b') # Redup
        
        edge_colors = []
        for _ in G.edges:
            if random.random() > 0.7:
                edge_colors.append('#0284c7') # Garis transfer data aktif (Biru)
            else:
                edge_colors.append('#1e293b') # Standby gelap
                
        nx.draw(G, pos, ax=ax, node_color=node_colors, with_labels=False, 
                node_size=250, edge_color=edge_colors, width=0.5, arrows=False)
        ax.axis('off')

    print("⏳ Sedang merender animasi .gif...")
    ani = animation.FuncAnimation(fig, update, frames=12, interval=300, repeat=True)
    ani.save('neural_network_animation.gif', writer='pillow', fps=3.5)
    plt.close()
    print("✅ ANIMASI SUKSES DISIMPAN: 'neural_network_animation.gif'")

buat_animasi()