class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        
        count = defaultdict(int)
        good = 0

        for i, n in enumerate(nums):

            if i - n in count:
                good += count[i - n]

            count[i - n] += 1
        
        return (len(nums) * (len(nums) - 1) // 2) - good

