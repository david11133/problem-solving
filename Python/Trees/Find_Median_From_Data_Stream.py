from heapq import heappush, heappop, heappushpop

class MedianFinder:
    def __init__(self):
        self.small = []  # Max-heap (inverted min-heap)
        self.large = []  # Min-heap

    def addNum(self, num: int) -> None:
        if len(self.small) == len(self.large):
            heappush(self.large, -heappushpop(self.small, -num))
        else:
            heappush(self.small, -heappushpop(self.large, num))

    def findMedian(self) -> float:
        if len(self.small) == len(self.large):
            print(self.large[0], "/", self.small[0])
            return float(self.large[0] - self.small[0]) / 2.0
        else:
            return float(self.large[0])

# Example usage:
medianFinder = MedianFinder()
medianFinder.addNum(1)
medianFinder.addNum(5)
print(medianFinder.findMedian())  # Output: 3.0
medianFinder.addNum(2)
print(medianFinder.findMedian())  # Output: 2.0
medianFinder.addNum(4)
print(medianFinder.findMedian())  # Output: 3.0
