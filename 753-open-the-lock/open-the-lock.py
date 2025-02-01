class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        if "0000" in deadends:
            return -1
        
        q = deque([("0000", 0)])
        visit = set(deadends)
        visit.add("0000")

        def children(lock):
            res = []
            for i in range(4):
                digit = str((int(lock[i]) + 1) % 10) 
                res.append(lock[:i] + digit + lock[i + 1:])
                digit = str((int(lock[i]) - 1 + 10) % 10) 
                res.append(lock[:i] + digit + lock[i + 1:])

            return res

        while q:
            lock, key = q.popleft()

            if lock == target:
                return key
            
            for child in children(lock):
                if child in visit:
                    continue
                q.append((child, key + 1))
                visit.add(child)
        return -1

        