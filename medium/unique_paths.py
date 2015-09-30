
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # m: row, n: column
        result = [[1]*m for i in xrange(n)]
        for y in xrange(1, m):
            for x in xrange(1, n):
                result[x][y] = result[x-1][y] + result[x][y-1]
        return result[-1][-1]

def main():
    inputs = [(3,7)]
    for m, n in inputs:
        result = Solution().uniquePaths(m, n)
        print result

if __name__ == '__main__':
    main()
