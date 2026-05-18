import heapq

class MedianFinder:

    def __init__(self):
        self.small = []   # max heap
        self.large = []   # min heap

    def addNum(self, num):

        # Push into max heap
        heapq.heappush(self.small, -num)

        # Ensure ordering
        if self.large and -self.small[0] > self.large[0]:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # Balance heaps
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        if len(self.large) > len(self.small):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def findMedian(self):

        # Odd length
        if len(self.small) > len(self.large):
            return float(-self.small[0])

        # Even length
        return (-self.small[0] + self.large[0]) / 2.0