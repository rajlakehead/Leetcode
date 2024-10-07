class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preReqMap = {}

        for i in range(numCourses):
            preReqMap[i] = []

        for crs, pre in prerequisites:
            preReqMap[crs].append(pre)
        
        visit = set()
        
        def dfs(crs):
            if preReqMap[crs] == []:
                return True
            
            if crs in visit:
                return False

            visit.add(crs)

            for pre in preReqMap[crs]:
                if not dfs(pre):
                    return False
            
            preReqMap[crs] = []
            visit.remove(crs)

            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True