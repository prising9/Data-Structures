
import time

arr = [1,2,5,6,89,45,32,21,34,3,6,9, 91,23]

PIVOT_END = 1
PIVOT_MID = 2

"""
Quick sort picks a pivot and makes two partitions: one with elements less than and the
other with elements greater than pivot. Combining the two 
	[low] + [pivot] + [high] 
recursively reducing the partitions gives us a sorted array. 

Time complexity : Avg/best case = O(n log n)
Worst case (for a sorted array) : O(n**2)
"""	
def quicksort(arr, pivot_choice):
	if len(arr) <= 1:
		return arr
	hi = []
	lo = []
	pivot = arr[-1]
	lenarr = len(arr)-1
	#print(f"Picked pivot = {pivot} lenarr {lenarr}")
	for i in range(0,lenarr):
		if arr[i] > pivot:
			hi.append(arr[i])
		else:
			lo.append(arr[i])
	#print(arr)
	#print(lo, pivot, hi)

	return(quicksort(lo, pivot_choice) + [pivot] + quicksort(hi, pivot_choice))

start_time = time.time()
sortedarr = quicksort(arr, PIVOT_END)
end_time = time.time()

print(f"Len of arr {arr} = {len(arr)}")
print(f"Len of sorted array = {sortedarr} {len(sortedarr)}")
print(f"Time taken END pivot is {end_time-start_time:0.8f} sec or {((end_time-start_time)*10**6):0.2f} microsec")

start_time = time.time()
sortedarr = quicksort(arr, PIVOT_MID)
end_time = time.time()
print(f"Time taken MID pivot is {end_time-start_time:0.8f} sec or {((end_time-start_time)*10**6):0.2f} microsec")