class Solution:
       def minimumArrayLength(self, A: List[int]) -> int:
        v = min(A)
        for x in A:
            if x % v:
                return 1
        return (A.count(v) + 1) // 2