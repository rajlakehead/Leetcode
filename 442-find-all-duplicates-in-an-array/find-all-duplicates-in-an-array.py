class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []

        for n in nums:
            num = abs(n)
            if nums[num - 1] < 0:
                ans.append(num)
            nums[num - 1] *= -1
        return ans

        