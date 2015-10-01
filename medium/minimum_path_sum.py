
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        path = [[0]*n for i in xrange(m)]

        path[0][0] = grid[0][0]
        for x in xrange(1, m):
            path[x][0] = path[x-1][0] + grid[x][0]
        for y in xrange(1, n):
            path[0][y] = path[0][y-1] + grid[0][y]

        for x in xrange(1, m):
            for y in xrange(1, n):
                v = grid[x][y]
                path[x][y] = min(path[x-1][y] + v, path[x][y-1] + v)
        return path[-1][-1]

def main():
    inputs = [[[1,2],[1,1]], [[1]]]
    for grid in inputs:
        result = Solution().minPathSum(grid)
        print result

if __name__ == '__main__':
    main()
