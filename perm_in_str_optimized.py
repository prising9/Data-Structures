from collections import defaultdict

class Solution:
    def check_subsequent_str(self, substr, s1,map1):
        map2 = defaultdict(int)
        for i in range(0,len(substr)):
            map2[substr[i]] +=1
        
        if map1 != map2:
            return False
        return True

    def checkInclusion(self, s1: str, s2: str) -> bool:

        n1 = len(s1) 
        n2 = len(s2)

        if n1 > n2:
            return False
        
        map1 = defaultdict(int)
        for i in range(n1):
            map1[s1[i]] +=1

        i = 0
        #Find the 1st letter in s2 that also is in s1
        while i < n2:
            if s2[i] in s1:
                if (self.check_subsequent_str(s2[i:i+n1], s1, map1)):
                    return True
            i+=1
        return False

