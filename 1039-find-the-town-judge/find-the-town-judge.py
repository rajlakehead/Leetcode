class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if not trust and n == 1:
            return 1

        hashmap = defaultdict(int)
        hashmap_two = defaultdict(int)

        for a, b in trust:
            hashmap[b] += 1
            hashmap_two[a] += 1
        
        for k, v in hashmap.items():
            print(k, v)
            if hashmap[k] == n - 1 and hashmap_two[k] == 0:
                return k
        return -1
