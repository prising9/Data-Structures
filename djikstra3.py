#from heapq import heapify, heappush, heappop
import heapq

graph = {	'A' :{ 'B':3, 'C':3},
			'B' :{ 'A':3, 'E':2.8, 'D':3.5 },
			'C' :{ 'A':3, 'E':2.8, 'F':3.5 },
			'D' :{ 'B':3.5, 'E':3.1, 'G':10 },

			'E' :{ 'G':7, 'C':2.8, 'B':2.8, 'D':3.1 },
			'F' :{ 'C':3.5, 'G':2.5 },
			'G' :{ 'F':2.5, 'E':7, 'D':10 },
		}

INFINITY = 1000

def find_path(start, end, distances):
	
def find_shortest_path(start, end):
	all_from_start = {}  	# Every Node -> distance from start
	visited = [] 			# list of nodes visited
	for node in graph.keys():
		all_from_start[node] = INFINITY
	all_from_start[start] = 0 #Set beginning node  distance from start to 0

	pq = []
	heapq.heappush(pq, (0, start))

	while (pq):
		d, curr = heapq.heappop(pq)
		if curr in visited:
			continue

		curr_dist = all_from_start[curr]
		#print(f"Visiting curr = {curr} curr_dist = {curr_dist}")

		for  neigh,wt in graph[curr].items():

			dist = curr_dist + wt  

			#update the global distances if this path is shorter
			if dist < all_from_start[neigh]:
				all_from_start[neigh] = dist

			#heapq prioritises on 1st value in tuple. so dist first
			heapq.heappush(pq, (dist, neigh)) #add neighbor to heapq

		visited.append(curr)
	print(f"distances from {start} : ")
	print(all_from_start)

	print(find_path(start, end, distances))


if __name__ == '__main__' :
	find_shortest_path('B', 'F')