from collections import defaultdict

class Solution:

    def permute(self, s, ndx, N, arr):
        #print(f"N is {N} ndx={ndx}")
        if (ndx == N):
            arr.append(s.copy())
            #print(s)
            return
        
        for i in range(ndx, N+1):
            s[ndx], s[i] = s[i], s[ndx]
            self.permute(s, ndx+1, N, arr)
            s[ndx], s[i] = s[i], s[ndx]
        #print(arr)
        return (arr)

    def checkInclusion(self, s1: str, s2: str) -> bool:

        #Check1 : first just check if all letters are present in 2nd string
        map1 = defaultdict(int)
        n = len(s1) 
        for i in range (0,n):
            map1[s1[i]] += 1
        
        map2 = defaultdict(int)
        n2 = len(s2)
        for i in range (0, n2):
            map2[s2[i]] += 1
        
        for i in range (0,n):
            if map1[s1[i]] > map2[s1[i]]:
                return False
        
        #Find the 1st letter in s2 that also is in s1
        for i in range(0,n2):
            if s2[i] in s1:
                print(f"{s2[i]} is in {s1} at pos {i}")
                break
        
        #check that the next n letters in s2 all belong to s1
        for j in range(i, n2-1):
            print (f"Checking {s2[j]}")
            if s2[j] not in s1:
                return False

        '''arr = []

        self.permute(list(s1), 0, len(s1)-1, arr)
        for item in arr:
            str = ''.join(item)
            #print(f"Checking if {str} is in {s2}")
            if str not in s2:
                continue
            else:
                return True 

        return (False) '''
        return True


