import heapq
from collections import defaultdict

graph = {	'A' :{ 'B':3, 'C':3},
			'B' :{ 'A':3, 'E':2.8, 'D':3.5 },
			'C' :{ 'A':3, 'E':2.5, 'F':3.5 },
			'D' :{ 'B':3.5, 'E':3.1, 'G':10 },

			'E' :{ 'G':7, 'C':2.5, 'B':2.8, 'D':3.1 },
			'F' :{ 'C':3.5, 'G':2.5 },
			'G' :{ 'F':2.5, 'E':7, 'D':10 },
		}

INFINITY = 1000

def get_path(parents, start,end):
	path = []

	node = end
	while node != start:
		path.insert(0,node)
		node = parents[node]
	path.insert(0,node)
	return(path)


def djikstra(graph, start, end):
	distances = {}
	pq = []
	visited = []
	parents = {}

	for node in graph.keys():
		distances[node] = INFINITY

	heapq.heappush(pq, (0,start))
	distances[start] = 0

	while(pq):
		d, node = heapq.heappop(pq)

		if (node) in visited:
			continue

		if (node == end):
			visited.append(node)
			break
		curr_dist = distances[node]

		for neigh,wt in graph[node].items():

			if (wt+curr_dist) < distances[neigh]:
				distances[neigh] = wt+curr_dist
				parents[neigh] = node
			heapq.heappush(pq,(distances[neigh], neigh))
		if node not in visited:
			visited.append(node)
	print(visited)
	print(get_path(parents, start,end))

start = 'A'
end= 'G'

print(f"start = {start} end = {end}")
djikstra(graph, start,end)
