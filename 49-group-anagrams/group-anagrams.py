class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for word in strs:
            w = "".join(sorted(word))
            
            if w in hashmap:
                hashmap[w].append(word)
            else:
                hashmap[w].append(word)
        return hashmap.values()
            
        