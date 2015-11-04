
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        import operator
        S = [str(i) for i in xrange(1, n+1)]
        N = reduce(operator.mul, xrange(1, n+1))
        return self.getPermutation_0(n, k-1, S, N)

    def getPermutation_0(self, n, k, S, N):
        if n == 1:
            return S[0]

        d = N / n
        q, r = divmod(k, d)
        x = S.pop(q)
        return x + self.getPermutation_0(n-1, r, S, d)

def main():
    inputs = [(4, 24),]
    for n, k in inputs:
        for i in xrange(1, k+1):
            result = Solution().getPermutation(n, i)
            print result

if __name__ == '__main__':
    main()
