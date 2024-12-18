graph = {	'A' :{ 'B':3, 'C':3},
			#'B' :{ 'A':3, 'E':2.8, 'D':3.5 },
			'B' :{ 'A':3 },
			'C' :{ 'A':3, 'E':2.5, 'F':3.5 },
			'D' :{ 'B':3.5, 'E':3.1, 'G':10 },

			'E' :{ 'G':7, 'C':2.5, 'B':2.8, 'D':3.1 },
			'F' :{ 'C':3.5, 'G':2.5 },
			'G' :{ 'F':2.5, 'E':7, 'D':10 },
			#'H' : {}
		}


def is_connected(graph, start,end):
	visited = []
	all = []
	all = graph.keys()
	print(all)
	q = []

	q.append(start)

	while q:
		node = q.pop(0)
		for neigh in graph[node]:
			if neigh not in visited:
				q.append(neigh)
		if node not in visited:
			visited.append(node)

	print(f"Visited = {visited}")
	if end in visited:
		print(f"{start} is connected to {end}!")
	else:
		print(f"{start} NOT connected to {end}!")

	#print(set(visited).intersection(set(all)))
	if (len(set(visited).intersection(set(all))) == len(all)):
		print(f"The whole graph is connected")
	else:
		print(f"The graph is not connected {len(all)}")

if __name__ == '__main__':
	start = 'C'
	end = 'B'
	is_connected(graph, start, end)