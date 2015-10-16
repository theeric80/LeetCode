
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums:
            return self.findDuplicate_2(nums)

    def findDuplicate_2(self, nums):
        # binary search
        lo, hi = 1, len(nums)-1
        while lo < hi:
            mid = (lo+hi) / 2
            count = sum(n<=mid for n in nums)
            if count <= mid:
                lo = mid + 1
            else:
                hi = mid
        return lo

    def findDuplicate_1(self, nums):
        # cycle-finding: start from 0
        sz = len(nums)
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow = 0
        while True:
            slow = nums[slow]
            fast = nums[fast]
            if slow == fast:
                break
        return slow

    def findDuplicate_0(self, nums):
        # cycle-finding: start from sz-1
        sz = len(nums)
        slow, fast = sz-1, sz-1
        while True:
            slow = nums[slow]-1
            fast = nums[nums[fast]-1]-1
            if slow == fast:
                break
        slow = sz-1
        while True:
            slow = nums[slow]-1
            fast = nums[fast]-1
            if slow == fast:
                break
        return slow + 1

def main():
    inputs = [(1,2,3,1), (1,2,2), (1,3,4,2,2),]
    for nums in inputs:
        result = Solution().findDuplicate(nums)
        print result

if __name__ == '__main__':
    main()
