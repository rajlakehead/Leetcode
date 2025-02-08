class Solution:
    def numSquares(self, n: int) -> int:
        q = deque([(n, 0)])
        visited = set([n])
        
        while q:
            num, steps = q.popleft()  # Use popleft for BFS
            
            # If num is a perfect square, we can add one more step and return.
            if math.sqrt(num) == int(math.sqrt(num)):
                return steps + 1
            
            # Try subtracting all possible squares.
            for i in range(1, int(math.sqrt(num)) + 1):
                next_val = num - i * i
                if next_val not in visited:
                    visited.add(next_val)
                    q.append((next_val, steps + 1))
                    
        # Although the problem guarantees a solution, return -1 if something goes wrong.
        
        


        