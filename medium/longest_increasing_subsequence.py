
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums:
            return self.lengthOfLIS_0(nums)
        return 0

    def lengthOfLIS_0(self, nums):
        # O(n2)
        result = 1
        n = len(nums)
        dp = [1] * n
        for i in xrange(n):
            ni = nums[i]
            for j in xrange(i):
                if ni > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
            result = max(result, dp[i])
        return result

def main():
    inputs = [[10, 9, 2, 5, 3, 7, 101, 18],]
    for nums in inputs:
        result = Solution().lengthOfLIS(nums)
        print result

if __name__ == '__main__':
    main()
