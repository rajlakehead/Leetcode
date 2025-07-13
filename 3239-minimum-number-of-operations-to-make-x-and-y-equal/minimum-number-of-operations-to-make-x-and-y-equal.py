class Solution:
    def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:
        if y >= x:
            return y - x

        q = collections.deque()
        q.append((x, 0))
        visited = set()

        while q:
            for _ in range(len(q)):
                num, steps = q.popleft()

                if num == y:
                    return steps
                
                if num not in visited:
                    
                    visited.add(num)

                    if num % 11 == 0:
                        q.append((num // 11, steps + 1))
                    if num % 5 == 0:
                        q.append((num // 5, steps + 1))
                    
                    q.append((num - 1, steps + 1))
                    q.append((num + 1, steps + 1))
            

