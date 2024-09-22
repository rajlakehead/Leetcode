class Solution:
    def maxWidthRamp(self, A: List[int]) -> int:
        ans = 0
        stack = []

        for i in range(len(A)):
            if not stack or A[stack[-1]] > A[i]:
                stack.append(i)
            
        for i in range(len(A) - 1, -1, -1):
            while stack and A[stack[-1]] <= A[i]:
                ans = max(ans, i - stack.pop())
        return ans