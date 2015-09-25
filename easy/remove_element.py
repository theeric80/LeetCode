
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        j = len(nums)
        for i, n in enumerate(nums):
            if n != val:
                continue
            # swap two elements nums[i] and nums[j]
            # nums[j] is the last element that it's values doesn't equal to val
            if i >= j:
                break
            j -= 1
            while j > i and nums[j] == val:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        return j

def main():
    inputs = [([1, 1, 2, 2, 3, 4, 5], 1), ([4, 5], 5), ([3, 3], 3), ([1], 1)]
    for nums, val in inputs:
        result = Solution().removeElement(nums, val)
        print result, nums

if __name__ == '__main__':
    main()
