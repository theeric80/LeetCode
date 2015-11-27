
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix: return 0
        result = 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0]*n for i in xrange(m)]
        for i in xrange(m):
            for j in xrange(n):
                x = int(matrix[i][j])
                val = x
                if i == 0 or j == 0 or x == 0:
                    val = x
                else:
                    val = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                dp[i][j] = val
                result = max(result, val)

        for i in xrange(m):
            print dp[i]

        return result*result

def main():
    matrix = [['1','0','1','0','0'],
              ['1','0','1','1','1'],
              ['1','1','1','1','1'],
              ['1','0','0','1','0']]
    result = Solution().maximalSquare(matrix)
    print result

if __name__ == '__main__':
    main()
