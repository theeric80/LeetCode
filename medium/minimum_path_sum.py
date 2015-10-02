
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        path = [[0]*n for i in xrange(m)]

        path[0][0] = grid[0][0]
        for i in xrange(1, m):
            path[i][0] = path[i-1][0] + grid[i][0]
        for j in xrange(1, n):
            path[0][j] = path[0][j-1] + grid[0][j]

        for i in xrange(1, m):
            for j in xrange(1, n):
                v = grid[i][j]
                path[i][j] = min(path[i-1][j] + v, path[i][j-1] + v)
        return path[-1][-1]

def main():
    inputs = [[[1,2],[1,1]], [[1]]]
    for grid in inputs:
        result = Solution().minPathSum(grid)
        print result

if __name__ == '__main__':
    main()
