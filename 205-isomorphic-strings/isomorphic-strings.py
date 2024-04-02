class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hashmap = {}
        new_hashmap = {}
        
        for i in range(len(s)):
            c1, c2 = s[i], t[i]

            if (c1 in hashmap and hashmap[c1] != c2) or (c2 in new_hashmap and new_hashmap[c2] != c1):
                return False

            hashmap[c1] = c2
            new_hashmap[c2] = c1
            
        return True
        