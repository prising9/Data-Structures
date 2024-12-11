from collections import defaultdict

graph1 = {
	0:[2],
	2:[],
	1:[0,4,3],
	3:[4,5],
	4:[],
	5:[]
}

graph2 = {
	1: [2, 3],
	2: [3,4],
	3: [4,5],	
	6 : [1],
	7 : []
}

graph3 = {
	0:[1,2],
	2:[],
	1:[3,4],
	3:[4,5],
	4:[]	
}

graph4 = {
	5:[2,0],
	0:[],
	2:[3],
	3:[1],
	1:[],
	4:[0,1]
}

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


def top_sort_kahn(graph):
	indegree_zero = []

	#calculate indegree for each node
	indegrees = defaultdict(int)  #defaultdict initializes all keys

	for node,neighlist in graph.items():
		if not neighlist:
			indegrees[node] = 0
		for neigh in neighlist:
			indegrees[node]+=1

	print(f"The given graph is \n{graph}\n")
	print(f"Its Indegrees counts are {indegrees}\n")

	#add all nodes with indegree 0 to q
	for node,count in indegrees.items():
		if (count == 0):
			indegree_zero.append(node)

	#print(indegree_zero)
	top_sorted = []

	while indegree_zero:
		node = indegree_zero.pop(0)
		#print(f"Processing {node} from {indegree_zero}")

		top_sorted.append(node)

		#reduce the indegree for each of its neighbors
		for parent, neighlist in graph.items():
			if node in neighlist:
				indegrees[parent]-=1
				if indegrees[parent] <= 0:
					indegree_zero.append(parent)
	
	#If graph has edges left, it has a cycle (not DAG)
	if len(graph) != len(top_sorted):
		print(f"Not a DAG - has cycles")
	else:
		return(top_sorted)

print(f"Topological sort yields {top_sort_kahn(graph5)}")
