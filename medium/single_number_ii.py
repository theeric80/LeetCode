
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return
        return self.singleNumber_0(nums)

    def singleNumber_0(self, nums):
        result = 0
        mask = 1
        for i in xrange(32):
            b = sum((n>>i) & mask for n in nums) % 3
            result |= (b << i)
        return self.sign(result)

    def sign(self,x):
        return x if x < 2**31 else x-2**32

def main():
    inputs = [(-2147483648,), (-4,), (1,1,1,3,3,3,5), (1,)]
    for nums in inputs:
        result = Solution().singleNumber(nums)
        print result

if __name__ == '__main__':
    main()
