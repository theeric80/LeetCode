
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        f = [0] * (n+1)
        f[0] = f[1] = 1
        for i in xrange(2, n+1):
            f[i] = sum(f[j] * f[i-j-1] for j in xrange(0, i))
        return f[n]

def main():
    inputs = [3, 4]
    for n in inputs:
        result = Solution().numTrees(n)
        print result

if __name__ == '__main__':
    main()
