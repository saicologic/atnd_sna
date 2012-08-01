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

G = nx.Graph()

# 自分が参加したイベントを取得する。
events = utils.get_event_by_user(user_id)

# 自分が参加したイベントの人物ネットワークを作成する。
c = 0
for event in events:
  if c < len(events):
    utils.add_network(G, event.event_id)
    c +=1
    print '----------------------------------------------------------------------------'

# pajeckに出力をする。
utils.save_graph(G, user_id)

# グラフを描画する。
nx.draw(G)
plt.show()