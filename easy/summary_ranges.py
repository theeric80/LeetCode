
class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        i=0
        sz = len(nums)
        result = []
        for j in xrange(0, sz-1):
            a, b = nums[j], nums[j+1]
            if (b-a) > 1:
                result.append('{}->{}'.format(nums[i], a) if j > i else str(a))
                i = j + 1

        if i < sz:
            j = sz - 1
            a = nums[j]
            result.append('{}->{}'.format(nums[i], a) if j > i else str(a))
        return result

def main():
    inputs = [[], [0], [0,1,2,4,5,7], [0,1,2,4,5], [0,1,2,4,7]]
    for nums in inputs:
        result = Solution().summaryRanges(nums)
        print result

if __name__ == '__main__':
    main()
