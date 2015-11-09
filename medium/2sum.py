
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        return self.twoSum_2(nums, target)

    def twoSum_2(self, nums, target):
        # hash table
        S = dict()
        for i, a in enumerate(nums, 1):
            b = target - a
            if b in S:
                return sorted([i, S[b]])
            S[a] = i

    def twoSum_1(self, nums, target):
        n = len(nums)
        N = zip(nums, xrange(1, n+1))
        N.sort()
        for i in xrange(n-1):
            a = N[i][0]
            if a > 0 and a > target: break

            for j in xrange(i+1, n):
                b = N[j][0]
                sum_ = a + b
                if sum_ == target:
                    return sorted([N[i][1], N[j][1]])
                elif sum_ > target:
                    break

    def twoSum_0(self, nums, target):
        n = len(nums)
        for i in xrange(n-1):
            a = nums[i]
            for j in xrange(i+1, n):
                b = nums[j]
                sum_ = a + b
                if sum_ == target:
                    return sorted([i+1, j+1])

def main():
    inputs = [([2,7,11,15], 9), ([3,2,4], 6), ([-1,-2,-3,-4,-5], -8)]
    for nums, target in inputs:
        result = Solution().twoSum(nums, target)
        print result

if __name__ == '__main__':
    main()
