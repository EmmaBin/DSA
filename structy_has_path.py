#Write a function, has_path, that takes in a dictionary representing the adjacency list 
#of a directed acyclic graph and two nodes (src, dst). 
#The function should return a boolean indicating whether or not there exists a directed path between the source and destination nodes.

# graph = {
#   'f': ['g', 'i'],
#   'g': ['h'],
#   'h': [],
#   'i': ['g', 'k'],
#   'j': ['i'],
#   'k': []
# }

# has_path(graph, 'f', 'k') # True


#DFS
def has_path(graph, src, dst):
  stack = [ src ]
  while len(stack)>0:
    curr = stack[-1]
    if curr == dst:
      return True
    stack.pop()
    for neighbor in graph[curr]:
      stack.append(neighbor)
  return False

#BFS
from collections import deque

def has_path(graph, src, dst):
  queue = deque([ src ])
  
  while queue:
    current = queue.popleft()
    
    if current == dst:
      return True
    
    for neighbor in graph[current]:
      queue.append(neighbor)
    
  return False

n = number of nodes
e = number edges
Time: O(e)
Space: O(n)

#recursively 
def has_path(graph, src, dst):
  if src == dst:
    return True
  
  for neighbor in graph[src]:
    if has_path(graph, neighbor, dst) == True:
      return True
    
  return False
n = number of nodes
e = number edges
Time: O(e)
Space: O(n)


#以下是自己做出来的，没有用recursion的方法，注意要点在visited set，如果去过就重新开始iteration
#stack最后会为空，跳出while loop. 没找到就是false
def undirected_path(edges, node_A, node_B):
  graph = convert_to_graph(edges)
  stack=[node_A]
  visited = set()
  while len(stack)>0:
    curr = stack[-1]
    stack.pop()
    if curr == node_B:
      return True
    if curr in visited:
      continue
    else:
      visited.add(curr)
  
    for neighbor in graph[curr]:
      stack.append(neighbor)
  return False

def convert_to_graph(edges):
  graph={}
  for edge in edges:
    a, b = edge
    if a not in graph:
      graph[a]=[]
    if b not in graph:
      graph[b] =[]
    graph[a].append(b)
    graph[b].append(a)
  
  return graph