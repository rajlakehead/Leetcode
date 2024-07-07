class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for word in strs:
            w = "".join(sorted(word))
            hashmap[w].append(word)
            
        return hashmap.values()
            
        