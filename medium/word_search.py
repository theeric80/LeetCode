
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
        for i in xrange(m):
            for j in xrange(n):
                if self.exist_0(board, word, [], i, j):
                    return True
        return False

    def exist_0(self, board, word, path, i, j):
        if not word:
            return True

        m, n = len(board), len(board[0])
        if i < 0 or i >= m or j < 0 or j >= n:
            return False

        ch = board[i][j]
        if ch != word[0]:
            return False

        path.append((i, j))
        next_steps = [(i, j-1), (i, j+1), (i-1, j), (i+1, j)]
        for next_step in next_steps:
            if next_step in path:
                continue
            if self.exist_0(board, word[1:], path, *next_step):
                return True
        path.pop()
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
