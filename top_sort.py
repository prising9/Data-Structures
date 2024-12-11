def get_all(graph):
	all_nodes = []

	# First make a list of all connected nodes
	for node,neighList in graph.items():
		if node not in all_nodes:
			all_nodes.append(node)

		for neigh in neighList:
			if neigh not in all_nodes:
				all_nodes.append(neigh)
	print(f"All nodes are : {all_nodes} Graph {graph1}")
	return(all_nodes)

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

def add_sorted(graph, node, all_nodes, ordered_list):
	ordered_list.append(node)
	if node in all_nodes:
		all_nodes.remove(node)
	if node in graph.keys():
		del graph[node]

def top_srt(graph):
	all_nodes = get_all(graph)	  #list of all nodes in graph
	ordered_list = []             #added in top order
	node = list(graph)[0]

	while all_nodes:
		# If graph is gone, the remaining nodes don't have any incoming edges
		if not graph: 				# Add rest of the nodes from all_nodes to ordered list
			remaining_nodes = all_nodes[:]
			for node in remaining_nodes:
				add_sorted(graph, node,all_nodes, ordered_list)
			return(ordered_list)	

		new_parent = False
		print(f"Looping through all with Node = {node}")
		for start,neighlist in graph.items():
			if node in neighlist:
				print(f"Node {node} is in neighlist of {start}")
				node = start
				new_parent = True
				break #go to while all_nodes
		if new_parent:
			continue
		else:
			add_sorted(graph,node, all_nodes, ordered_list)
			print(f"Adding {node} to Sorted List {ordered_list}. Neighbor list now is {graph}")
			if (graph):
				node = list(graph)[0]

	return(ordered_list)

print(f"Ordered list is {top_srt(graph1)}")
print(f"Ordered list is {top_srt(graph2)}")
print(f"Ordered list is {top_srt(graph3)}")
print(f"Ordered list is {top_srt(graph4)}")


