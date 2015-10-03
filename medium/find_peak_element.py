
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # num[i] != num[i+1]
        # num[-1] = num[n] = negative infinity
        if not nums:
            return -1
        return self.findPeakElement_0(nums, 0, len(nums)-1)

    def findPeakElement_0(self, nums, lo, hi):
        if hi == lo:
            return lo

        mid = (lo+hi) / 2
        if nums[mid] > nums[mid+1]:
            # nums[lo ... mid] must has a peak
            # 1) nums[mid-1] < nums[mid] -> nums[mid] is a peak
            # 2) nums[mid-1] > nums[mid] -> nums[lo ... mid-1] has a peak
            return self.findPeakElement_0(nums, lo, mid)
        else:
            return self.findPeakElement_0(nums, mid+1, hi)

def main():
    inputs = [[1, 2, 3, 1], [], [1,], [1,2,3]]
    for nums in inputs:
        print nums
        result = Solution().findPeakElement(nums)
        print result

if __name__ == '__main__':
    main()
