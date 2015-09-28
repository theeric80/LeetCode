
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return self.productExceptSelf_2(nums)

    def productExceptSelf_2(self, nums):
        sz = len(nums)
        result = [1] * sz
        for i in xrange(1, sz):
            result[i] = result[i-1] * nums[i-1]

        right = 1
        for i in xrange(sz-1, -1, -1):
            result[i] *= right
            right *= nums[i]
        return result

    def productExceptSelf_1(self, nums):
        # space: O(n)
        sz = len(nums)
        a = [1] * sz
        b = [1] * sz
        # a: a0 * a1 * ... * an-1 * an
        # b: an * an-1 * ... * a1 * a0
        for i in xrange(1, sz):
            a[i] = a[i-1] * nums[i-1]
            b[i] = b[i-1] * nums[sz-i]

        result = [1] * sz
        for i in xrange(0, sz):
            result[i] = a[i] * b[sz-1-i]
        return result

    def productExceptSelf_0(self, nums):
        # O(n^2)
        from operator import mul
        sz = len(nums)
        result = [1] * sz
        for i in xrange(sz):
            result[i] = reduce(mul, (nums[j] for j in xrange(sz) if j != i))
        return result

def main():
    inputs = [(1,2,3,4), (2,4,6)]
    for nums in inputs:
        result = Solution().productExceptSelf(nums)
        print result

if __name__ == '__main__':
    main()
