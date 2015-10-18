class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        m, n = len(board), len(board[0])
        row = [[0]*n for i in xrange(m)]
        col = [[0]*n for i in xrange(m)]
        sqr = [[0]*n for i in xrange(m)]

        for i in xrange(m):
            for j in xrange(n):
                val = board[i][j]
                if val == '.':
                    continue
                val = int(val)-1
                if row[i][val] > 0:
                    return False
                if col[val][j] > 0:
                    return False
                x, y = i/3, j/3
                if sqr[x*3 + y][val] > 0:
                    return False
                row[i][val] = col[val][j] = sqr[x*3 + y][val] = 1

        return True

def main():
    board = [
        "..4...63.",
        ".........",
        "5......9.",
        "...56....",
        "4.3.....1",
        "...7.....",
        "...5.....",
        ".........",
        "........."]
    result = Solution().isValidSudoku(board)
    print result

if __name__ == '__main__':
    main()
