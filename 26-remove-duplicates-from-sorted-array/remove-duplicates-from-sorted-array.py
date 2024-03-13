class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        hashset = set()
        newarr = []
        i = 0

        for n in nums:
            if n not in hashset:
                nums[i] = n
                hashset.add(n)
                i += 1
        


        return i 
            
        