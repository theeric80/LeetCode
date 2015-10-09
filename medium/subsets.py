
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result, subset = [[]], []
        if nums:
            self.subsets_1(sorted(nums), result)
            #self.subsets_0(sorted(nums), 0, subset, result)
        return result

    def subsets_1(self, nums, result):
        sz = len(nums)
        for n in nums:
            result += [s+[n] for s in result]

    def subsets_0(self, nums, i, subset, result):
        sz = len(nums)
        if i >= sz:
            return

        for j in xrange(i, len(nums)):
            n = nums[j]
            subset.append(n)
            result.append(subset[:])
            self.subsets_0(nums, j+1, subset, result)
            subset.pop()

def main():
    inputs = [[1,2,3], [4,1,0]]
    for nums in inputs:
        result = Solution().subsets(nums)
        print result

if __name__ == '__main__':
    main()
