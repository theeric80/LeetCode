
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return
        self.rotate_0(matrix)
        #self.anti_rotate(matrix)

    def anti_rotate(self, matrix):
        # anticlockwise rotate
        # 1) reverse left to right 2) swap the symmetry
        m, n = len(matrix), len(matrix[0])
        """
        for j in xrange(n/2):
            for i in xrange(m):
                matrix[i][j], matrix[i][n-1-j] = matrix[i][n-1-j], matrix[i][j]
        """
        for i in xrange(m):
            matrix[i].reverse()

        for j in xrange(1, n):
            for i in xrange(0, j):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    def rotate_0(self, matrix):
        # clockwise rotate
        # 1) reverse up to down 2) swap the symmetry
        m, n = len(matrix), len(matrix[0])
        """
        for i in xrange(m/2):
            for j in xrange(n):
                matrix[i][j], matrix[m-1-i][j] = matrix[m-1-i][j], matrix[i][j]
        """
        matrix.reverse()

        for j in xrange(1, n):
            for i in xrange(0, j):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

def main():
    inputs = [[[1,2,3], [4,5,6], [7,8,9]], [[1,2],[3,4]], []]
    for matrix in inputs:
        print matrix
        Solution().rotate(matrix)
        print matrix

if __name__ == '__main__':
    main()
