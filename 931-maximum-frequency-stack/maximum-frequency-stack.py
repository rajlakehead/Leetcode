class FreqStack:

    def __init__(self):
        self.heap = []
        self.count = defaultdict(int)
        self.index = 0
        

    def push(self, val: int) -> None:
        self.count[val] += 1
        heapq.heappush(self.heap, (-self.count[val], -self.index, val))
        self.index += 1
        
    def pop(self) -> int:
        _, _, num = heapq.heappop(self.heap)
        self.count[num] -= 1

        return num

        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()