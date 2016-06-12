
class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        _sums = [0]
        for n in nums:
            _sums += [_sums[-1] + n]
        self._sums = _sums

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self._sums[j+1] - self._sums[i]

def main():
    nums = [-2, 0, 3, -5, 2, -1]
    solution = NumArray(nums)

    inputs = [(0,2), (2,5),(0,5)]
    for i, j in inputs:
        result = solution.sumRange(i, j)
        print result

if __name__ == '__main__':
    main()
