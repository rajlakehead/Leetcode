from sortedcontainers import SortedList

class MyCalendar:
    def __init__(self):
        self.calendar = SortedList()

    def book(self, start: int, end: int) -> bool:
        idx = bisect.bisect_left(self.calendar, (start, end))

        if idx > 0 and self.calendar[idx - 1][1] > start:
            return False
        
        # Check if it overlaps with the next event
        if idx < len(self.calendar) and self.calendar[idx][0] < end:
            return False
        
        # No conflict, insert the new interval
        self.calendar.add((start, end))
        return True