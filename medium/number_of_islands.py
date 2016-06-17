
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid: return 0

        m, n = len(grid), len(grid[0])
        marked = [[False] * n for i in xrange(m)]
        id = [[0] * n for i in xrange(m)]
        count = 0

        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j] == '1' and not marked[i][j]:
                    count += 1
                    self.dfs(grid, i, j, marked, id, count)

        for r in id:
            print r
        return count

    def dfs(self, grid, i, j, marked, id, count):
        m, n = len(grid), len(grid[0])

        marked[i][j] = True
        id[i][j] = count

        adjs = [(i, j-1), (i, j+1), (i-1, j), (i+1, j)]
        for x, y in adjs:
            if x < 0 or x >= m or y < 0 or y >= n: continue
            if not marked[x][y] and grid[x][y] == '1':
                self.dfs(grid, x, y, marked, id, count)

def main():
    grid = [
        '11110',
        '11010',
        '11000',
        '00000']

    grid = [list(r) for r in grid]
    result = Solution().numIslands(grid)
    print '# of islands = {}'.format(result)

    grid = [
        '11000',
        '11000',
        '00100',
        '00011']

    grid = [list(r) for r in grid]
    result = Solution().numIslands(grid)
    print '# of islands = {}'.format(result)

if __name__ == '__main__':
    main()
