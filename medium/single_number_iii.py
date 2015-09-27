
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return
        return self.singleNumber_0(nums)

    def singleNumber_1(self, nums):
        # bit manipulation: A xor A = 0
        a_xor_b = 0
        for x in nums:
            a_xor_b ^= x

        # The last bit that a differs b
        last_bit = (a_xor_b & (a_xor_b-1)) ^ a_xor_b

        a, b = 0, 0
        for x in nums:
            # Base on the last bit, group the nums into groupA(include a) and groupB
            if x & last_bit:
                a ^= x
            else:
                b ^= x
        return a, b

    def singleNumber_0(self, nums):
        # hash table
        result = 0
        h = {}
        for x in nums:
            h[x] = True if x in h else False
        return filter(lambda x: not h[x], h.iterkeys())

def main():
    inputs = [(1,2,1,3,4,3), (1,2)]
    for nums in inputs:
        result = Solution().singleNumber(nums)
        print result

if __name__ == '__main__':
    main()
