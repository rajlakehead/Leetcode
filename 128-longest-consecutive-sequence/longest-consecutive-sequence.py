class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashmap = defaultdict(int)
        nums = set(nums)
        ans = 0

        for n in nums:
            left = hashmap[n - 1]
            right = hashmap[n + 1]
            length = 1 + left + right


            hashmap[n - left] = length
            hashmap[n + right] = length

            ans = max(ans, length)

        
        return ans
