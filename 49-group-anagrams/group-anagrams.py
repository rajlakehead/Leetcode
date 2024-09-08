class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}

        for s in strs:
            new_s = "".join(sorted(s))

            if new_s in hashmap:
                hashmap[new_s].append(s)
            else:
                hashmap[new_s] = [s]

        return hashmap.values()
        