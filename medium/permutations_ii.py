
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result, perm = [], []
        nums.sort()
        self.permuteUnique_0(nums, perm, result)
        return result

    def permuteUnique_0(self, nums, perm, result):
        sz = len(nums)
        if not nums:
            result.append(perm[:])
            return

        for i in xrange(sz):
            n = nums[i]
            if i <= 0 or n != nums[i-1]:
                perm.append(n)
                self.permuteUnique_0(nums[:i]+nums[i+1:], perm, result)
                perm.pop()

def main():
    inputs = [[1,1,2],[1,2,1],[]]
    for nums in inputs:
        result = Solution().permuteUnique(nums)
        print result

if __name__ == '__main__':
    main()
