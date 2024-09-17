class TimeMap:

    def __init__(self):
        self.hashmap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        lst = self.hashmap[key]
        left, right = 0, len(lst)
        if not lst or timestamp < lst[0][0]:
            return ""
        while left < right:

            mid = (left + right) // 2

            if lst[mid][0] <= timestamp:
                left = mid + 1
            else:
                right = mid
        
        return lst[mid][1]





# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)