
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return
        self.setZeroes_1(matrix)

    def setZeroes_1(self, matrix):
        # space: O(1)
        # use the first row and column to store states
        m, n = len(matrix), len(matrix[0])

        m0 = 0 if any(matrix[0][i]==0 for i in xrange(n)) else 1
        n0 = 0 if any(matrix[i][0]==0 for i in xrange(m)) else 1

        for i in xrange(1, m):
            for j in xrange(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0

        for i in xrange(1, m):
            for j in xrange(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if m0 == 0:
            for j in xrange(n):
                matrix[0][j] = 0

        if n0 == 0:
            for i in xrange(m):
                matrix[i][0] = 0

    def setZeroes_0(self, matrix):
        # space: O(m + n)
        m, n = len(matrix), len(matrix[0])
        row = [1] * m
        col = [1] * n
        for i in xrange(m):
            for j in xrange(n):
                if matrix[i][j] == 0:
                    row[i] = col[j] = 0

        for i in xrange(m):
            for j in xrange(n):
                if row[i] == 0 or col[j] == 0:
                    matrix[i][j] = 0

def main():
    inputs = [[[1,0],[1,1]], [[1]], [], [[0,1]], [[1,1,1],[0,1,2]]]
    for matrix in inputs:
        print matrix
        Solution().setZeroes(matrix)
        print matrix

if __name__ == '__main__':
    main()
