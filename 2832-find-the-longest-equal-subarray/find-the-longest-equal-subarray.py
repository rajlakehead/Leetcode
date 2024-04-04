class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        res = 1
        left = 0
        count = defaultdict(int)
        currmax = 0

        for right in range(len(nums)):
            count[nums[right]] += 1
            currmax = max(currmax, count[nums[right]])

            while (right - left + 1) - currmax > k:
                count[nums[left]] -= 1
                left += 1
                if count[nums[left]] == 0:
                    del count[nums[left]]
            
        return currmax
                


        