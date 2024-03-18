class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        def binary_search(s):
            if potions[-1] * s < success:
                return len(potions)
            left = 0
            right = len(potions) - 1

            while left < right:
                mid = (left + right) // 2

                if potions[mid] * s >= success:
                    right = mid
                else:
                    left = mid + 1
            
            return left
        
        res = []
        for s in spells:
            idx = binary_search(s)
            res.append(len(potions) - idx)

        return res
        
        