
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return
        return self.singleNumber_0(nums)

    def singleNumber_1(self, nums):
        # bit manipulation: A xor A = 0
        result = 0
        for x in nums:
            result ^= x
        return result

    def singleNumber_0(self, nums):
        # hash table
        result = 0
        h = {}
        for x in nums:
            h[x] = True if x in h else False
        return filter(lambda x: not h[x], h.iterkeys())[0]

def main():
    inputs = [(1,1,3,2,3), (1,)]
    for nums in inputs:
        result = Solution().singleNumber(nums)
        print result

if __name__ == '__main__':
    main()
