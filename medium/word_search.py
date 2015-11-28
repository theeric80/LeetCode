
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board:
            return False

        m, n = len(board), len(board[0])
        visited = [[0]*n for i in xrange(m)]
        for i in xrange(m):
            for j in xrange(n):
                visited[i][j] = 1
                if self.exist_0(board, word, visited, i, j):
                    return True
                visited[i][j] = 0
        return False

    def exist_0(self, board, word, visited, i, j):
        if not word:
            return True

        m, n = len(board), len(board[0])
        if i < 0 or i >= m or j < 0 or j >= n:
            return False

        ch = board[i][j]
        if ch != word[0]:
            return False

        visited[i][j] = 1
        next_steps = [(i, j-1), (i, j+1), (i-1, j), (i+1, j)]
        for x, y in next_steps:
            if x < 0 or x >= m or y < 0 or y >= n:
                continue
            if visited[x][y] == 1:
                continue
            if self.exist_0(board, word[1:], visited, x, y):
                return True
        visited[i][j] = 0
        return False


def main():
    board = [['A','B','C','E'],
             ['S','F','C','S'],
             ['A','D','E','E']]
    inputs = ['ABCCED', 'SEE', 'ABCB', 'A']
    for word in inputs:
        result = Solution().exist(board, word)
        print '{0}: {1}'.format(word, result)

if __name__ == '__main__':
    main()
