#DFS ensures that a node only gets added after its dependencies have been added first. This produces the topological ordering.

# Example DAG
graph5 = {
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

def top_sort_dfs(graph):
	stack = []
	visited = []

	for node in graph.keys():
		stack.insert(0,node)
		while(stack):
			dependent_parent = False
			node = stack.pop(0)      #get top element off stack
			for neigh in graph[node]: #visit each neighbor of node and see if already in visisted
				if neigh not in visited:
					if node not in stack:
						dependent_parent = True
						stack.insert(0,node) #push the parent node back
					stack.insert(0,neigh)

			if len(graph[node]) == 0 and node not in visited:    #empty neighbor, no dependency
				print(f"Empty neigh, added node {node} to visited")
				visited.append(node)
				continue
			if not dependent_parent and node not in visited:
				visited.append(node)
			print(f"added node {node} to visited")

	return visited




print(f"Topological sort yields {top_sort_dfs(graph5)}")

