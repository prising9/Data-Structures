# Example DAG
graph1 = {
  'A': ['D'],
  'B': ['D'],
  'C': ['A', 'B'],
  'D': ['G', 'H'],
  'E': ['F'],
  'F': ['H'],
  'G': [],
  'H': [],
  #'H': ['D']  #uncomment to create a cycle for a non DAG
}

graph2 = {
  1: [2, 3],
  2: [3,4],
  3: [4,5], 
  4: [5],
  5: [],
  6 : [1],
  7 : [5]
}

graph3 = {
  1: [2, 3],
  2: [3,4],
  3: [4,5], 
  6 : [1],
  7 : [5]
}

def top_sort_dfs(graph, vertex, visited):

  #To handle the case when a vertex listed as a neighbor is not in the graph keys
  #Treat as a node in the graph without neighbors. e.g nodes 4,5 in graph3
  if vertex not in graph.keys():
    visited.append(vertex)
    return
  
  #First push all neighbors so they're visited before current vertex
  for neigh in graph[vertex]:
      if neigh not in visited:
        top_sort_dfs(graph, neigh, visited)
  #Now all neighbors are visited, and can also mark the current vertex as visited
  if vertex not in visited:
    visited.append(vertex)

def top_sort_driver(graph):
  visited = []

  for v in graph.keys():
    top_sort_dfs(graph, v, visited)

  print(f"Topological sort of graph = \n{graph} is \n{visited}")


top_sort_driver(graph1)
top_sort_driver(graph2)
top_sort_driver(graph3)

