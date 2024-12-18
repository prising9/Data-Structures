graph = {	'A' :{ 'B':3, 'C':3},
			'B' :{ 'A':3, 'E':2.8, 'D':3.5 },
			'C' :{ 'A':3, 'E':2.5, 'F':3.5 },
			'D' :{ 'B':3.5, 'E':3.1, 'G':10 },

			'E' :{ 'G':7, 'C':2.5, 'B':2.8, 'D':3.1 },
			'F' :{ 'C':3.5, 'G':2.5 },
			'G' :{ 'F':2.5, 'E':7, 'D':10 },
		}


stack = []
visited = []

def dfs(graph, node, end):
	if (node == end and node not in visited):
		visited.append(end)
		#print(f"Found {end}")
		return True
	if node not in visited:
		stack.insert(0, node)
	while stack :
		node = stack.pop(0)
		visited.append(node)
		for neigh,wt in graph[node].items():
			if(dfs(graph, neigh, end) == True):
				return True
	return False


'''
DFS search from start to end node in graph
'''
if __name__ == "__main__" :

	#start = list(graph.keys())[0]
	start = 'A'
	end='F'

	if (dfs(graph, start, end) == True):
		print(f"Found {end}")
	else:
		print(f"Not found {end}")
	print(visited)
