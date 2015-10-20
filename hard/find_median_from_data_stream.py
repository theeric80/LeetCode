
class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._data = []

    def _binarySearch(self, n):
        lo, hi = 0, len(self._data)-1
        while lo <= hi:
            mid = (lo+hi) / 2
            if n < self._data[mid]:
                hi = mid - 1
            elif n > self._data[mid]:
                lo = mid + 1
            else:
                return mid
        return lo

    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        i = self._binarySearch(num)
        self._data.insert(i, num)

    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        if not self._data: return

        sz, i = len(self._data), len(self._data)/2
        if (sz%2) == 0:
            return (self._data[i-1]+self._data[i]) / 2.0
        else:
            return self._data[i]

def main():
    inputs = [(1,2), (1,2,3),()]
    for nums in inputs:
        mf = MedianFinder()
        for n in nums:
            mf.addNum(n)
        result = mf.findMedian()
        print nums, result

if __name__ == '__main__':
    main()
