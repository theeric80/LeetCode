
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        self.quicksort(nums, 0, len(nums)-1)

    def sortColors_1(self, nums):
        zero, second = 0, len(nums)-1
        for i, n in enumerate(nums):
            if i > second:
                break
            while nums[i] == 0:
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1
            while nums[i] == 2:
                nums[i], nums[second] = nums[second], nums[i]
                second -= 1

    def quicksort(self, nums, lo, hi):
        if lo < hi:
            p = self.partition(nums, lo, hi)
            self.quicksort(nums, lo, p)
            self.quicksort(nums, p+1, hi)

    def partition(self, A, p, r):
        # Hoare-Partition
        x = A[p]
        i = p - 1
        j = r + 1
        while True:
            while True:
                j -= 1
                if A[j] <= x: break
            while True:
                i += 1
                if A[i] >= x: break
            if i < j:
                A[i], A[j] = A[j], A[i]
            else:
                return j

def main():
    inputs = [[2,0,1,2],]
    for nums in inputs:
        Solution().sortColors(nums)
        print nums

if __name__ == '__main__':
    main()
