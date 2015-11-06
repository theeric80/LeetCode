
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()
        n = len(nums)
        for i in xrange(n-3):
            a = nums[i]
            if i > 0 and a == nums[i-1]: continue
            for j in xrange(i+1, n-2):
                b = nums[j]
                if j > i+1 and b == nums[j-1]: continue
                lo, hi = j+1, n-1
                while lo < hi:
                    c, d = nums[lo], nums[hi]
                    sum_ = a + b + c + d
                    if sum_ == target:
                        result.append([a, b, c, d])
                        while lo < hi and nums[lo] == nums[lo+1]: lo += 1
                        while lo < hi and nums[hi] == nums[hi-1]: hi -= 1
                        lo += 1
                        hi -= 1
                    elif sum_ < target:
                        lo += 1
                    else:
                        hi -= 1
        return result

    def threeSum(self, nums, target):
        result = []
        nums.sort()
        n = len(nums)
        for i in xrange(n-2):
            a = nums[i]
            lo, hi = i+1, n-1
            while lo < hi:
                b, c = nums[lo], nums[hi]
                sum_ = a + b + c
                if sum_ == target:
                    result.append([a, b, c])
                    lo += 1
                    hi -= 1
                elif sum_ < target:
                    lo += 1
                else:
                    hi -= 1
        return result

def main():
    inputs = [([1,0,-1,0,-2,2], 0), ([-1,0,-5,-2,-2,-4,0,1,-2], -9),]
    for nums, target in inputs:
        result = Solution().fourSum(nums, target)
        print result

if __name__ == '__main__':
    main()
