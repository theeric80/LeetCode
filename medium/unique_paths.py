
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        result = [[1]*n for i in xrange(m)]
        for i in xrange(1, m):
            for j in xrange(1, n):
                result[i][j] = result[i-1][j] + result[i][j-1]
        return result[-1][-1]

def main():
    inputs = [(3,7)]
    for m, n in inputs:
        result = Solution().uniquePaths(m, n)
        print result

if __name__ == '__main__':
    main()
