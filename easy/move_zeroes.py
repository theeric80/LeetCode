
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return nums
        return self.moveZeroes_0(nums)

    def moveZeroes_1(self, nums):
        i = 0
        for j, n in enumerate(nums):
            if n != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1

    def moveZeroes_0(self, nums):
        i, j = 0, 0
        sz = len(nums)
        while True:
            while i < sz and nums[i] != 0:
                i += 1
            j = max(j, i+1)
            while j < sz and nums[j] == 0:
                j += 1
            if i >= sz or j >= sz:
                break
                continue
            nums[i], nums[j] = nums[j], nums[i]

def main():
    inputs = [[1, 0], [1, 1, 0], [0, 1, 0, 3, 12], [0], [1], [0, 0], [1, 1]]
    for nums in inputs:
        Solution().moveZeroes(nums)
        print nums 

if __name__ == '__main__':
    main()
