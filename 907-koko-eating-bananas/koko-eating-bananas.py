class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        left, right = 1, piles[-1]

        def condition(speed):
            time = 0

            for p in piles:
                time += (math.ceil(p / speed))
                if time > h:
                    return False
            return True

        while left < right:
            mid = left + (right - left) // 2

            if condition(mid):
                right = mid
            else:
                left = mid + 1
        return left