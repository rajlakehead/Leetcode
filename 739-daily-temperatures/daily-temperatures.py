class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(temperatures)

        for idx, tempt in enumerate(temperatures):

            while stack and temperatures[stack[-1]] < tempt:
                index = stack.pop()
                ans[index] = (idx - index)
            
            stack.append(idx)
        return ans


        