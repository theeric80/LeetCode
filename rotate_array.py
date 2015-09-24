
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if k <= 0 or k == len(nums):
            return
        self.rotate_1(nums, k)

    def rotate_1(self, nums, k):
        sz = len(nums)
        self.reverse(nums, 0, sz-1)
        self.reverse(nums, 0, (k-1) % sz)
        self.reverse(nums, k % sz, sz-1)

    def reverse(self, nums, i, j):
        sz = (j-i+1) / 2
        for c in xrange(sz):
            a, b = i+c, j-c
            nums[a], nums[b] = nums[b], nums[a]

    def rotate_0(self, nums, k):
        # slow solution
        j = len(nums)-1
        for c in xrange(k):
            n = nums[j]
            for i in xrange(j-1, -1, -1):
                nums[i+1] = nums[i]
            nums[0] = n

def main():
    inputs = [([-1], 2), ([1,2], 2), ([], 0), ([1], 1), ([1,2,3,4,5,6,7], 3)]
    for nums, k in inputs:
        Solution().rotate(nums, k)
        print nums

if __name__ == '__main__':
    main()
