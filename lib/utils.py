# -*- coding:utf-8 -*-

# http://api.atnd.org/
# http://api.atnd.org/events/users/?event_id=31128

import sys
import os
import pprint
import json
import networkx as nx
import matplotlib.pyplot as plt

pp = pprint.PrettyPrinter(indent=4)
atnd = os.path.join(os.path.abspath('../'), 'lib')
sys.path.insert(0, atnd)

from atnd4p import *

def debug_user(user):
  print str(user.user_id) + "\t" + str(user.nickname)

def get_owner_in_event(event_id):
  query = {}
  query['event_id'] = event_id
  atnd = get_atnd("EVENTS",query)
  event = atnd.events[0]
  owner = {
    'id': event.owner_id,
    'user_id': event.owner_id,
    'nickname': event.owner_nickname,
  }
  return owner

def add_node(g, user):
  user_id = user['id']
  
  g.add_node(user_id)
  g.node[user_id] = {
    'id': user['user_id'],
    'user_id': user['user_id'],
    'nickname': user['nickname'],
  }

def add_edge(g, owner, user):
  print str(owner['id']) + "\t" + str(user['id'])
  g.add_edge(owner['id'], user['id'])
  
def add_network(g, event_id):
  query = {}
  query['event_id'] = event_id

  owner = get_owner_in_event(event_id)
  owner_id = owner['id']
  print owner
  add_node(g, owner)
  
  atnd = get_atnd("USERS",query)
  for event in atnd.events:
    for u in event.users:
      # 出席者のみを抽出
      if u.status == 1:
        user = {
          'id': u.user_id,
          'user_id': u.user_id,
          'nickname': u.nickname,
        }
        add_edge(g, owner, user)
        add_node(g, user)
        debug_user(u)

def get_event_by_user(user_id):
  query = {}
  query['user_id'] = user_id
  atnd = get_atnd("EVENTS",query)
  return [event for event in atnd.events]


def ranking(data):
  return sorted(data.items(), key=lambda x:x[1], reverse=True)

def get_node_by_user(g, user_id):
  node = g.node[user_id]
  return {
    'user_id': node['user_id'],
    'nickname': node['nickname'],
  }
def show_user(user):
  return "%s\t\t%s" % (user['user_id'], user['nickname'])
  
def show_ranking(g, boundary, data, limit=10):
  c = 0
  print boundary + '--------------------------------'
  print "RANK\tUSERID\t\tNICKNAME"
  for user_id, v in ranking(data):
    if c < limit:
      
      rank = str(c+1) + "\t"
      if boundary == 'edge_betweenness_centrality':
        print rank + str(show_user(get_node_by_user(g, user_id[0])))
        print rank + str(show_user(get_node_by_user(g, user_id[1])))
        print '--------------------------------------------------------------------------'
      else:
        print rank + str(show_user(get_node_by_user(g, user_id)))
      c +=1
    else:
      break

  print boundary + '--------------------------------'
  print ''

def filename(user_id, ext='net'):
  return 'result_' + str(user_id) + '.' + ext

def save_graph(g, user_id):
  nx.write_pajek(g, filename(user_id))
  
def read_graph(user_id):
  nx.path_graph(4)
  return nx.read_pajek(filename(user_id))

def write_graph(g, user_id):
  nx.draw(g)
  plt.savefig(filename(user_id, 'png'))