
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        return self.nextPermutation_0(nums)

    def nextPermutation_1(self, nums):
        # Find the largest index k such that a[k] < a[k+1]
        # Find the largest index l greater than k such that a[k] < a[l]
        # Swap the value of a[k] with that of a[l]
        # Reverse the sequence from a[k+1] up to and including the final element a[n]
        n = len(nums)
        for k in xrange(n-2, -1, -1):
            if nums[k] < nums[k+1]:
                l = n - 1
                while l > k and nums[l] <= nums[k]:
                    l -= 1
                nums[k], nums[l] = nums[l], nums[k]
                self.reverse(nums, k+1, n-1)
                return
        nums.reverse()

    def reverse(self, nums, lo, hi):
        n = hi - lo + 1
        for i in xrange(0, n/2):
            nums[lo+i], nums[hi-i] = nums[hi-i], nums[lo+i]

    def nextPermutation_0(self, nums):
        sz = len(nums)
        for i in xrange(sz-2, -1, -1):
            if nums[i] < nums[i+1]:
                self.insertion_sort(nums, i+1, sz-1)
                j = i + 1
                while j < sz and nums[j] <= nums[i]:
                    j += 1
                nums[i], nums[j] = nums[j], nums[i]
                return
        nums.reverse()

    def insertion_sort(self, nums, lo, hi):
        for i in xrange(lo+1, hi+1):
            for j in xrange(i, lo, -1):
                if nums[j-1] <= nums[j]: break
                nums[j-1], nums[j] = nums[j], nums[j-1]

def main():
    inputs = [[1,2,3], [3,2,1], [1,1,5], [1,3,2], [2,3,1]]
    for nums in inputs:
        Solution().nextPermutation(nums)
        print nums

if __name__ == '__main__':
    main()
