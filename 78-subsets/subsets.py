class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(index, lst):
            if index >= len(nums):
                res.append(lst.copy())
                return
            
            lst.append(nums[index])
            backtrack(index + 1, lst)

            lst.remove(nums[index])
            backtrack(index + 1, lst)

        backtrack(0, [])
        return res
        