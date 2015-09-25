
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        v, i = nums[0], 1
        for j, n in enumerate(nums):
            if n > v:
                nums[i], nums[j] = nums[j], nums[i]
                v = nums[i]
                i += 1
        return i

def main():
    inputs = [[1, 1, 2, 2, 3, 4, 4, 5], [4, 5], [3, 3], [1]]
    for nums in inputs:
        result = Solution().removeDuplicates(nums)
        print result, nums

if __name__ == '__main__':
    main()
