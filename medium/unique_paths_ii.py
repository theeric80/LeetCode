
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        return self.uniquePathsWithObstacles_0(obstacleGrid)

    def uniquePathsWithObstacles_1(self, obstacleGrid):
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        path = [[0]*(n+1) for i in xrange(m+1)]
        path[0][1] = 1
        for i in xrange(1, m+1):
            for j in xrange(1, n+1):
                if obstacleGrid[i-1][j-1] == 0:
                    path[i][j] = path[i-1][j] + path[i][j-1]
        return path[-1][-1]

    def uniquePathsWithObstacles_0(self, obstacleGrid):
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        path = [[0]*n for i in xrange(m)]

        i, j = 0, 0
        while i < m and obstacleGrid[i][0] == 0:
            path[i][0] = 1
            i += 1
        while j < n and obstacleGrid[0][j] == 0:
            path[0][j] = 1
            j += 1
        for i in xrange(1, m):
            for j in xrange(1, n):
                if obstacleGrid[i][j] == 0:
                    path[i][j] = path[i-1][j] + path[i][j-1]
        return path[-1][-1]

def main():
    inputs = [[0,0,0], [0,1,0], [0,0,0]]
    result = Solution().uniquePathsWithObstacles(inputs)
    print result

if __name__ == '__main__':
    main()
