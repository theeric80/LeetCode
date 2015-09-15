
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
            while j > i:
                j -= 1
                if nums[j] == val:
                    continue
                nums[i], nums[j] = nums[j], nums[i]
                break
        return j

def main():
    inputs = [1, 1, 2, 2, 1, 3, 4, 1, 5]
    result = Solution().removeElement(inputs, 1)
    print result, inputs

if __name__ == '__main__':
    main()
