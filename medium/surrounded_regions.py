
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board: return
        m, n = len(board), len(board[0])

        for i in xrange(m):
            if board[i][0] == 'O':
                self.bfs(board, i, 0)
            if board[i][n-1] == 'O':
                self.bfs(board, i, n-1)

        for j in xrange(n):
            if board[0][j] == 'O':
                self.bfs(board, 0, j)
            if board[m-1][j] == 'O':
                self.bfs(board, m-1, j)

        for i in xrange(m):
            for j in xrange(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == '1':
                    board[i][j] = 'O'

    def bfs(self, board, i, j):
        m, n = len(board), len(board[0])
        q = [(i, j)]
        board[i][j] = '1'

        while q:
            i, j = q.pop(0)
            adjs = [(i, j-1), (i, j+1), (i-1, j), (i+1, j)]
            for x, y in adjs:
                if x < 0 or x >= m or y < 0 or y >= n: continue
                if board[x][y] == 'O':
                    board[x][y] = '1'
                    q.append((x, y))

def main():
    board = [
        ['X', 'X', 'X', 'X'],
        ['X', 'O', 'O', 'X'],
        ['X', 'X', 'O', 'X'],
        ['X', 'O', 'X', 'X']]

    Solution().solve(board)
    for r in board:
        print r

    board0 = [
        'XOOOOOOOOOOOOOOOOOOO',
        'OXOOOOXOOOOOOOOOOOXX',
        'OOOOOOOOXOOOOOOOOOOX',
        'OOXOOOOOOOOOOOOOOOXO',
        'OOOOOXOOOOXOOOOOXOOX',
        'XOOOXOOOOOXOXOXOXOXO',
        'OOOOXOOXOOOOOXOOXOOO',
        'XOOOXXXOXOOOOXXOXOOO',
        'OOOOOXXXXOOOOXOOXOOO',
        'XOOOOXOOOOOOXXOOXOOX',
        'OOOOOOOOOOXOOXOOOXOX',
        'OOOOXOXOOXXOOOOOXOOO',
        'XXOOOOOXOOOOOOOOOOOO',
        'OXOXOOOXOXOOOXOXOXOO',
        'OOXOOOOOOOXOOOOOXOXO',
        'XXOOOOOOOOXOXXOOOXOO',
        'OOXOOOOOOOXOOXOXOXOO',
        'OOOXOOOOOXXXOOXOOOXO',
        'OOOOOOOOOOOOOOOOOOOO',
        'XOOOOXOOOXXOOXOXOXOO']

    board = [list(row) for row in board0]
    for r in board:
        print r

    Solution().solve(board)
    for r in board:
        print r

if __name__ == '__main__':
    main()
