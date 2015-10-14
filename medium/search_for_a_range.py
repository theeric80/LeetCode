
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if nums:
            return self.searchRange_0(nums, target)
        return []

    def searchRange_0(self, nums, target):
        sz = len(nums)
        mid = self.search(nums, target, 0, sz-1)
        if mid < 0:
            return [-1, -1]

        i = lo = mid
        while True:
            i = self.search(nums, target, 0, i-1)
            if i < 0:
                break
            lo = i

        j = hi = mid
        while True:
            j = self.search(nums, target, j+1, sz-1)
            if j < 0:
                break
            hi = j

        return [lo, hi]

    def search(self, nums, target, lo, hi):
        while lo <= hi:
            mid = (lo+hi) / 2
            if target < nums[mid]:
                hi = mid - 1
            elif target > nums[mid]:
                lo = mid + 1
            else:
                return mid
        return -1

def main():
    inputs = [([5, 7, 7, 8, 8, 10], 8), ([2, 2], 2),]
    for nums, target in inputs:
        result = Solution().searchRange(nums, target)
        print result

if __name__ == '__main__':
    main()
