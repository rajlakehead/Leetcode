class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {}
        visit = set()
        path = set()
        res = []

        for i in range(numCourses):
            preMap[i] = []
        
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        def dfs(crs):
            if crs in visit:
                return True
            if crs in path:
                return False

            path.add(crs)

            for pre in preMap[crs]:
                if not dfs(pre): return False

            visit.add(crs)
            res.append(crs)
            path.remove(crs)

            return True

        
        for crs in range(numCourses):
            if not dfs(crs): return []
        return res