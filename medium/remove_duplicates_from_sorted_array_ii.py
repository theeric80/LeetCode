
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.removeDuplicates_0(nums)

    def removeDuplicates_1(self, nums):
        i = 0
        for n in nums:
            if i < 2 or n > nums[i-2]:
                nums[i] = n
                i += 1
        return i

    def removeDuplicates_0(self, nums):
        if len(nums) <= 2:
            return
        i, j = 2, 2
        sz = len(nums)
        while i < sz:
            if nums[i] < nums[i-1] or nums[i] == nums[i-2]:
                if nums[i-1] == nums[i-2]:
                    while j < sz and nums[j] <= nums[i-1]:
                        j += 1
                else:
                    while j < sz and nums[j] < nums[i-1]:
                        j += 1
                if j >= sz:
                    break
                nums[i], nums[j] = nums[j], nums[i]
            i += 1
        return i

def main():
    inputs = [[1,1,1,2,2,3], [1], [1,2], [1,2,3]]
    for nums in inputs:
        print nums
        result = Solution().removeDuplicates(nums)
        print nums, result

if __name__ == '__main__':
    main()
