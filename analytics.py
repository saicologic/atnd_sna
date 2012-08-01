# -*- coding:utf-8 -*-
import sys
import os
import networkx as nx
import matplotlib.pyplot as plt

lib = os.path.join(os.path.abspath('.'), 'lib')
sys.path.insert(0, lib)

import utils

# USER:saicologic
user_id = 1502

# G = nx.Graph()
G = utils.read_graph(user_id)

# undirected graph

# 次数中心性
utils.show_ranking(G, 'degree_centrality', nx.degree_centrality(G))

# 近接中心性
utils.show_ranking(G, 'closeness_centrality', nx.closeness_centrality(G))

# 媒介中心性
utils.show_ranking(G, 'betweenness_centrality', nx.betweenness_centrality(G))

# 媒介中心性(組)
utils.show_ranking(G, 'edge_betweenness_centrality', nx.edge_betweenness_centrality(G))

# 固有ベクトル中心性
# utils.show_ranking(G, 'eigenvector_centrality', nx.eigenvector_centrality(G))
  
# グラフを描画する。
nx.draw(G)
plt.show()

# グラフを画像で出力する。
# utils.write_graph(G, user_id)