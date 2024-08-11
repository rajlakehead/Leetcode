class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        visited = set()

        def dfs(r, c, prevHeight, ocean):

            if min(r, c) < 0 or r >= len(heights) or c >= len(heights[0]) or (r, c) in visited:
                return False
                
            if heights[r][c] > prevHeight:
                return False
            


            if ocean == "Pacific":
                if c == 0 or r == 0:
                    return True
            if ocean == "Atlantic":
                if r == len(heights) - 1 or c == len(heights[0]) - 1:
                    return True
                
            
            
            
            
            visited.add((r, c))
            
            res = dfs(r + 1, c, heights[r][c], ocean) or dfs(r, c + 1, heights[r][c], ocean) or dfs(r - 1, c, heights[r][c], ocean) or dfs(r, c - 1, heights[r][c], ocean)

            visited.remove((r, c))

            return res

        result = []
        
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if dfs(i, j, float('inf'), "Pacific") and dfs(i, j, float('inf'), "Atlantic"):
                    result.append([i, j])
        return result

            

        