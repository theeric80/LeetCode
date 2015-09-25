
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        i, j = m-1, n-1
        k = m + n - 1
        while i >= 0 and j >= 0:
            x, y = nums1[i], nums2[j]
            if x > y:
                nums1[k] = x
                i -= 1
            else:
                nums1[k] = y
                j -= 1
            k -= 1

        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1

    def merge_0(self, nums1, m, nums2, n):
        for i in xrange(0, n):
            self.insert(nums1, m+i, nums2[i])

    def insert(self, nums, i, n):
        nums[i] = n
        for j in xrange(i, 0, -1):
            if nums[j-1] <= nums[j]:
                break
            nums[j-1], nums[j] = nums[j], nums[j-1]

def main():
    inputs = [[[1 , 3, 5, 0, 0, 0], [2, 4, 6]]]
    for num1, num2 in inputs:
        Solution().merge(num1, 3, num2, 3)
        print num1

if __name__ == '__main__':
    main()
