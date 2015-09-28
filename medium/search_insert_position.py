
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.searchInsert_1(nums, target)

    def searchInsert_1(self, nums, target):
        l, h = 0, len(nums)-1
        while l <= h:
            mid = (l+h) / 2
            if target < nums[mid]:
                h = mid - 1
            elif target > nums[mid]:
                l = mid + 1
            else:
                return mid
        return l

    def searchInsert_0(self, l, h, nums, target):
        if h < l:
            return l

        mid = (l+h) / 2
        if target < nums[mid]:
            return self.searchInsert_0(l, mid-1, nums, target)
        elif target > nums[mid]:
            return self.searchInsert_0(mid+1, h, nums, target)
        else:
            return mid

def main():
    nums = [1,3,5,6]
    inputs = [5, 2, 7, 0]
    for n in inputs:
        result = Solution().searchInsert(nums, n)
        print result

if __name__ == '__main__':
    main()
