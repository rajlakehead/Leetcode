class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        
        def check(val):
            store = 0

            for q in quantities:
                store += math.ceil(q / val)
                if store > n:
                    return False
            return True
        
        left, right = 1, max(quantities)

        while left < right:
            mid = left + (right - left) // 2

            if check(mid):
                right = mid
            else:
                left = mid + 1
        return left
            