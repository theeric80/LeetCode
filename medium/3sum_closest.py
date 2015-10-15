
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums:
            return self.threeSumClosest_0(nums, target)

    def threeSumClosest_0(self, nums, target):
        sz = len(nums)
        nums.sort()
        result = nums[0]+nums[1]+nums[-1] - target
        for i in xrange(sz-2):
            a = nums[i]
            lo, hi = i+1, sz-1
            while lo < hi:
                b, c = nums[lo], nums[hi]
                sum_ = a + b + c - target
                if sum_ == 0:
                    return sum_ + target

                if sum_ < 0:
                    lo += 1
                elif sum_ > 0:
                    hi -= 1
                result = sum_ if abs(sum_)<abs(result) else result
        return result + target
                

def main():
    inputs = [([-1,2,1,-4], 1)]
    for nums, target in inputs:
        result = Solution().threeSumClosest(nums, target)
        print result

if __name__ == '__main__':
    main()
