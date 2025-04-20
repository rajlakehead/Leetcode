class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        def check(force):
            balls, prevPos = 0, -inf

            for pos in position:
                if pos - prevPos >= force:
                    balls += 1
                    if balls == m:
                        return True
                    prevPos = pos
            return False
        
        left, right = 1, position[-1] - position[0] + 1

        while left < right:
            mid = (left + right) // 2
            
            if check(mid):
                left = mid + 1
            else:
                right = mid
        return left - 1

            