class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        #Boyer-Moore Algorithm
        res = []

        candidate1, candidate2 = None, None
        count1, count2 = 0, 0
        
        count = (len(nums) // 3) + 1

        # Step 1: Find potential candidates

        for n in nums:

            if n == candidate1:
                count1 += 1
            elif n == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = n, 1
            elif count2 == 0:
                candidate2, count2 = n, 1
            else:
                count1 -= 1
                count2 -= 1

        # Step 2: Verify the candidates
        count1, count2 = 0, 0
        for n in nums:
            if n == candidate1:
                count1 += 1
            elif n == candidate2:
                count2 += 1
        
        if count1 >= count:
            res.append(candidate1)
        if count2 >= count:
            res.append(candidate2)
        
        return res
        
        #Feq Counter
        count = (len(nums) // 3) + 1
        counter = Counter(nums)

        for key in counter:
            if counter[key] >= count:
                res.append(key)
        return res
        