
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        return self.minSubArrayLen_0(s, nums)

    def minSubArrayLen_0(self, s, nums):
        result = 0
        sz = len(nums)
        i, j, sum_ = 0, 1, nums[0]
        for i, n in enumerate(nums):
            while j < sz and sum_ < s:
                sum_ += nums[j]
                j += 1
            if sum_ >= s:
                result = min(result, j-i) if result else j-i
            sum_ -= n
        return result

def main():
    inputs = [(7,[2,3,1,2,4,3]), (2,[1])]
    for s, nums in inputs:
        result = Solution().minSubArrayLen(s, nums)
        print result

if __name__ == '__main__':
    main()
