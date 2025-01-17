
str = "abcd"

count = len(str)

#O(len!)
def permute(s,idx, N, arr):
	if idx == N:
		arr.append(s.copy())  #copy when appending mutable object
		return

	for i in range (idx, N+1):
		s[idx],s[i] = s[i], s[idx]
		permute(s, idx+1, N,arr)
		s[idx], s[i] = s[i],s[idx] 

if __name__ == "__main__":
	arr = []
	print(f"Trying to permuteute {str} of Len {count}")
	s = list(str)
	N = len(s)
	permute(s, 0, N-1, arr)
	print(arr)
