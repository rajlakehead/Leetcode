class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        hashmap = defaultdict(list)
        sorted_trips = sorted(trips, key=lambda x: x[1])
        last_stop = 0
        start = sorted_trips[0][1]
        for t in sorted_trips:
            hashmap[t[1]].append(t[0])
            hashmap[t[2]].append(-t[0])
            last_stop = max(last_stop, t[1], t[2])
        for i in range(start, last_stop + 1):
            capacity -= sum(hashmap[i])
            if capacity < 0:
                return False
        return True



