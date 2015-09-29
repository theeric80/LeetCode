
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.missingNumber_0(nums)

    def missingNumber_1(self, nums):
        # x xor x = 0
        result = 0
        for i, n in enumerate(nums):
            result ^= n
            result ^= i
        result ^= len(nums)
        return result

    def missingNumber_0(self, nums):
        # sum total
        sz = len(nums)
        result = sz * (sz+1) / 2
        for n in nums:
            result -= n
        return result

def main():
    inputs = [(0,), (0, 1, 3)]
    for nums in inputs:
        result = Solution().missingNumber(nums)
        print result

if __name__ == '__main__':
    main()
