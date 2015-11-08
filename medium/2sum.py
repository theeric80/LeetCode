
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        return self.twoSum_0(nums, target)

    def twoSum_0(self, nums, target):
        n = len(nums)
        for i in xrange(n-1):
            a = nums[i]
            for j in xrange(i+1, n):
                b = nums[j]
                sum_ = a + b
                if sum_ == target:
                    return sorted([i+1, j+1])

def main():
    inputs = [([2,7,11,15], 9), ([3,2,4], 6)]
    for nums, target in inputs:
        result = Solution().twoSum(nums, target)
        print result

if __name__ == '__main__':
    main()
