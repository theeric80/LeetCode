
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums:
            return self.maxProduct_1(nums)
        return 0

    def maxProduct_1(self, nums):
        # Time Limit Exceeded
        n = len(nums)
        result = nums[0]
        P = [[nums[0], 1]]
        for i in xrange(1, n):
            ni = nums[i]
            P.append([])
            for j in xrange(i+1):
                product = ni * P[i-1][j]
                P[i].append(product)
                result = max(result, product)
            P[i].append(1)
        return result

    def maxProduct_0(self, nums):
        from operator import mul
        n = len(nums)
        dp = nums[:]
        result = nums[0]
        for i in xrange(1, n):
            ni = nums[i]
            for j in xrange(i):
                product = reduce(mul, (nums[x] for x in xrange(j, i+1)))
                dp[i] = max(dp[i], product)
            result = max(result, dp[i])
        return result

def main():
    inputs = [[2,3,-2,4], [], [2],]
    inputs += [[-2,3,-4],]
    inputs += [[2,-5,-2,-4,3]]
    for nums in inputs:
        result = Solution().maxProduct(nums)
        print '{0}: {1}'.format(nums, result)

if __name__ == '__main__':
    main()
