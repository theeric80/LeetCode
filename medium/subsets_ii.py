
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums:
            return self.subsetsWithDup_0(nums)
        return []

    def subsetsWithDup_0(self, nums):
        nums.sort()
        result, prev_begin = [[]], 0
        for i, n in enumerate(nums):
            begin = prev_begin if i > 0 and nums[i]==nums[i-1] else 0
            prev_begin = len(result)
            #result += [x+[n] for x in result[j:]]
            for j in xrange(begin, len(result)):
                result.append(result[j]+[n])
        return result

def main():
    inputs = [[1,2,2], [4,1,0]]
    for nums in inputs:
        result = Solution().subsetsWithDup(nums)
        print result

if __name__ == '__main__':
    main()
