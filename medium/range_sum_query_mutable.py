
class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        if not nums: return

        n = len(nums)
        sz = self._size(n) + 1

        self._n = n
        self._nodes = [0] * sz

        # build segment-tree
        self._build(nums, 0, n-1, 1)

    def _size(self, n):
        import math
        h = int(math.ceil(math.log(n, 2))) + 1
        return pow(2, h) - 1

    def _build(self, nums, lo, hi, n):
        if lo == hi:
            self._nodes[n] = nums[lo]
            return

        mid = lo + (hi-lo)/2
        l = 2 * n

        self._build(nums, lo, mid, l)
        self._build(nums, mid+1, hi, l+1)

        self._nodes[n] = self._nodes[l] + self._nodes[l+1]

    def _update(self, i, val, lo, hi, n):
        if lo == hi:
            self._nodes[n] = val
            return

        mid = lo + (hi-lo)/2
        l = 2 * n

        if i <= mid:
            self._update(i, val, lo, mid, l)
        if i > mid:
            self._update(i, val, mid+1, hi, l+1)

        self._nodes[n] = self._nodes[l] + self._nodes[l+1]

    def _sumRange(self, i, j, lo, hi, n):
        if i <= lo and j >= hi:
            return self._nodes[n]

        mid = lo + (hi-lo)/2
        l = 2 * n

        result = 0
        if i <= mid:
            result += self._sumRange(i, j, lo, mid, l)
        if j > mid:
            result += self._sumRange(i, j, mid+1, hi, l+1)
        return result

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        self._update(i, val, 0, self._n-1, 1)

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self._sumRange(i, j, 0, self._n-1, 1)

def main():
    nums = [1,3,5]
    solution = NumArray(nums)

    i, j = 0, 2
    result = solution.sumRange(0, 2)
    print 'sumRange({}, {}) = {}'.format(i, j, result)

    solution.update(1, 2)

    result = solution.sumRange(0, 2)
    print 'sumRange({}, {}) = {}'.format(i, j, result)

if __name__ == '__main__':
    main()
