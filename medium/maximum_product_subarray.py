
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums:
            return self.maxProduct_2(nums)
        return 0

    def maxProduct_2(self, nums):
        result = nums[0]
        n = len(nums)
        dp = nums[:] + [1]
        p0, p1, count = 1, 1, 0
        for i in xrange(0, n):
            ni = nums[i]
            p0, p1 = p0*ni, p1*ni
            if ni == 0:
                dp[i] = 0
                p0, p1, count = 1, 1, 0
            elif ni < 0:
                count += 1
                if count == 1:
                    dp[i] = ni
                    p1 = 1
                elif count % 2 == 0:
                    dp[i] = p0
                else:
                    dp[i] = p1
            else:
                dp[i] = max(ni, ni * dp[i-1])
            result = max(result, dp[i])
        return result

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
    inputs = [[2,3,-2,4], [], [2], [0,2]]
    inputs += [[-2,3,-4],]
    inputs += [[2,-5,-2,-4,3]]
    inputs += [[1,0,-1,2,3,-5,-2]]
    for nums in inputs:
        result = Solution().maxProduct(nums)
        print '{0}: {1}'.format(nums, result)

if __name__ == '__main__':
    main()
