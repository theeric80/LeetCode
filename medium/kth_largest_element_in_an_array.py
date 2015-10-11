
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums:
            return None
        #return self.findKthLargest_0(nums, len(nums)-k, 0, len(nums)-1)
        return self.findKthLargest_1(nums, k)

    def findKthLargest_1(self, nums, k):
        # use swim, from left to right
        # use sink, from right to left

        # heapify by sink
        sz = len(nums)
        hi = sz - 1
        for i in xrange((hi-1)/2, -1, -1):
            self.heap_sink(nums, i, hi)

        # sort-down
        i = hi
        for i in xrange(hi, 0, -1):
            nums[0], nums[i] = nums[i], nums[0]
            if i <= (sz-k):
                return nums[i]
            self.heap_sink(nums, 0, i-1)
        return nums[0]

    def heap_swim(self, nums, k):
        while True:
            j = (k-1) / 2
            if j < 0 or nums[j] >= nums[k]:
                break
            nums[k], nums[j] = nums[j], nums[k]
            k = j

    def heap_sink(self, nums, k, hi):
        while True:
            j = 2*k + 1
            if j < hi and nums[j] < nums[j+1]:
                j += 1
            if j > hi or nums[k] >= nums[j]:
                break
            nums[k], nums[j] = nums[j], nums[k]
            k = j
                
    def findKthLargest_0(self, nums, k, lo, hi):
        # quicksort
        j = self.partition(nums, lo, hi)
        if k < j:
            return self.findKthLargest_0(nums, k, lo, j-1)
        elif k > j:
            return self.findKthLargest_0(nums, k, j+1, hi)
        else:
            return nums[j]

    def partition(self, nums, lo, hi):
        v = nums[lo]
        i, j = lo - 1, hi + 1
        while True:
            while True:
                j -= 1
                if nums[j] <= v: break
            while True:
                i += 1
                if nums[i] >= v: break
            if i < j:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                return j

def main():
    inputs = [([3,2,1,5,6,4], 2)]
    for nums, k in inputs:
        result = Solution().findKthLargest(nums, k)
        print result

if __name__ == '__main__':
    main()
