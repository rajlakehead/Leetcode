import heapq

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        # sort by start day
        events.sort(key=lambda x: x[0])
        n = len(events)
        i = 0                # index into sorted events
        attended = 0         # count of events attended
        day = 0              # current day pointer
        min_heap = []        # heap of end-days

        while i < n or min_heap:
            # if no available events, jump day to next event's start
            if not min_heap:
                day = max(day, events[i][0])
            # add all events starting today
            while i < n and events[i][0] == day:
                heapq.heappush(min_heap, events[i][1])
                i += 1
            # attend the event that ends earliest
            earliest_end = heapq.heappop(min_heap)
            if earliest_end >= day:
                attended += 1
                day += 1
            # discard any events already expired before next loop
            while min_heap and min_heap[0] < day:
                heapq.heappop(min_heap)

        return attended
