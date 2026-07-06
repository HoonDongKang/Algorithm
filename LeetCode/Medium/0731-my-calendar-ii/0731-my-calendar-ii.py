class MyCalendarTwo:

    def __init__(self):
        self.booked = []
        self.overlaps = []

    def book(self, startTime: int, endTime: int) -> bool:
        for (start, end) in self.overlaps:
            if max(startTime, start) < min(endTime, end):
                return False

        for (start, end) in self.booked:
            if max(startTime, start) < min(endTime, end):
                self.overlaps.append((max(startTime, start), min(endTime, end)))

        self.booked.append((startTime, endTime))
        return True