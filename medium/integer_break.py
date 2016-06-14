
class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        m = [1] * n
        for i in xrange(2, n):
            m[i] = max(j * m[i-j] for j in xrange(1, i+1))
        return max(j * m[n-j] for j in xrange(1, n))

def main():
    inputs = [2, 6, 10]
    for n in inputs:
        result = Solution().integerBreak(n)
        print 'n={}, result={}'.format(n, result)

if __name__ == '__main__':
    main()
