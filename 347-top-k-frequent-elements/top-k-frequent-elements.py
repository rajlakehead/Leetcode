class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        feq = defaultdict(int)

        for n in nums:
            feq[n] += 1
        
        sorted_feq = dict(sorted(feq.items(), key=lambda x:x[1], reverse=True))

        return list(sorted_feq.keys())[:k]


        