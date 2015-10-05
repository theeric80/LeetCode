
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.search_0(nums, target, 0, len(nums)-1)

    def search_1(self, nums, target, lo, hi):
        if hi < lo:
            return -1

        mid = (lo+hi) / 2
        if target == nums[mid]:
            return mid

        if nums[lo] < nums[mid]:
            if target >= nums[lo] and target < nums[mid]:
                return self.search_0(nums, target, lo, mid-1)
            else:
                return self.search_0(nums, target, mid+1, hi)
        else:
            if target > nums[mid] and target <= nums[hi]:
                return self.search_0(nums, target, mid+1, hi)
            else:
                return self.search_0(nums, target, lo, mid-1)

    def search_0(self, nums, target, lo, hi):
        if hi < lo:
            return -1

        mid = (lo+hi) / 2
        if target == nums[mid]:
            return mid

        v = nums[0]
        if (target >= v and nums[mid] >= v) or (target < v and nums[mid] < v):
            if target < nums[mid]:
                return self.search_0(nums, target, lo, mid-1)
            elif target > nums[mid]:
                return self.search_0(nums, target, mid+1, hi)
        elif target >= v and nums[mid] < v:
            return self.search_0(nums, target, lo, mid-1)
        elif target < v and nums[mid] >= v:
            return self.search_0(nums, target, mid+1, hi)
        else:
            assert 0

def main():
    inputs = [((4,5,6,7,0,1,2), 1),]
    for nums, target in inputs:
        result = Solution().search(nums, target)
        print result

if __name__ == '__main__':
    main()
