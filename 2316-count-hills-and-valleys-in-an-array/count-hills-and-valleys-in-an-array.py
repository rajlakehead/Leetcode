class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        stack = []
        ans = 0
        idx = 0

        while idx < len(nums) - 1:
            if nums[idx] == nums[idx + 1]:
                idx += 1
                continue
            
            if stack:
                if nums[idx] > stack[-1] and nums[idx] > nums[idx + 1]:
                    ans += 1
                elif nums[idx] < stack[-1] and nums[idx] < nums[idx + 1]:
                    ans += 1
            stack.append(nums[idx])
            idx += 1

        return ans 