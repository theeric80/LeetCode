
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        return self.maxSubArray_0(nums)

    def maxSubArray_0(self, nums):
        # DP
        # max_at_n[i]: the maximum subarray ending with nums[i]
        max_at_n = nums[0]
        result = nums[0]
        for n in nums[1:]:
            max_at_n = max_at_n + n if max_at_n > 0 else n
            result = max(result, max_at_n)
        return result

def main():
    inputs = [[], (1,), (-2,1,-3,4,-1,2,1,-5,4)]
    for nums in inputs:
        result = Solution().maxSubArray(nums)
        print result

if __name__ == '__main__':
    main()
