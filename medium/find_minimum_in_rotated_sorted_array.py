
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return
        return self.findMin_1(nums)

    def findMin_1(self, nums):
        l, h = 0, len(nums)-1
        while h >= l:
            mid = (l+h) / 2
            if nums[mid-1] > nums[mid]:
                return nums[mid]
            elif nums[mid] < nums[h]:
                h = mid-1
            elif nums[mid] > nums[h]:
                l = mid+1
            else:
                return nums[mid]

    def findMin_0(self, nums, l, h):
        if h < l:
            assert(0)

        mid = (l+h) / 2
        if nums[mid-1] > nums[mid]:
            return nums[mid]
        elif nums[mid] < nums[h]:
            return self.findMin_0(nums, l, mid-1)
        elif nums[mid] > nums[h]:
            return self.findMin_0(nums, mid+1, h)
        else:
            return nums[mid]

def main():
    inputs = [(4,5,6,7,0,1,2), (1,), (2,3), (4,3)]
    for nums in inputs:
        result = Solution().findMin(nums)
        print result

if __name__ == '__main__':
    main()
