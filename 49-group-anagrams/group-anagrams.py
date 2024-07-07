class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for word in strs:
            w = "".join(sorted(word))
            
            if w in hashmap:
                hashmap[w].append(word)
            else:
                hashmap[w] = [word]
        return hashmap.values()
            
        