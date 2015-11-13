
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums:
            return self.threeSum_0(nums)
        return []

    def threeSum_0(self, nums):
        result = []
        n = len(nums)
        nums.sort()
        for i in xrange(n-2):
            a = nums[i]
            if i > 0 and a == nums[i-1]: continue
            lo, hi = i+1, n-1
            while lo < hi:
                b, c = nums[lo], nums[hi]
                sum_ = a + b + c
                if sum_ == 0:
                    result.append([a, b, c])
                    while lo < hi and nums[lo] == nums[lo+1]: lo += 1
                    while lo < hi and nums[hi] == nums[hi-1]: hi -= 1
                    lo += 1
                    hi -= 1
                elif sum_ < 0:
                    lo += 1
                else:
                    hi -= 1
        return result

def main():
    inputs = [[-1,0,1,2,-1,-4]]
    inputs += [[-2,0,0,2,2]]
    for nums in inputs:
        result = Solution().threeSum(nums)
        print result

if __name__ == '__main__':
    main()
