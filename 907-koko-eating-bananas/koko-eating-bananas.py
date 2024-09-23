class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def condition(speed):
            time = 0
            for p in piles:
                t = math.ceil((p / speed))
                time += t
                if time > h:
                    return False
            return True
        
        left, right = 1, max(piles)

        while left < right:
            mid = left + (right - left) // 2

            if condition(mid):
                right = mid
            else:
                left = mid + 1
        return left