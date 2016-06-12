
class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        m = len(matrix)+1
        n = len(matrix[0])+1 if matrix else 0
        s = [[0]*n for i in xrange(m)]
        for i in xrange(1, m):
            for j in xrange(1, n):
                s[i][j] = (s[i-1][j] + s[i][j-1] - s[i-1][j-1] +
                        matrix[i-1][j-1])
        self._sums = s

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        s = self._sums
        return s[row2+1][col2+1] - s[row1][col2+1] - s[row2+1][col1] + s[row1][col1]

def main():
    dummy = NumMatrix([])

    matrix = [
        [3, 0, 1, 4, 2],
        [5, 6, 3, 2, 1],
        [1, 2, 0, 1, 5],
        [4, 1, 0, 1, 7],
        [1, 0, 3, 0, 5]
    ]
    solution = NumMatrix(matrix)

    inputs = [(2,1,4,3), (1,1,2,2), (1,2,2,4)]
    for r1, c1, r2, c2 in inputs:
        result = solution.sumRegion(r1, c1, r2, c2)
        print result

    matrix = [[-4, -5]]
    solution = NumMatrix(matrix)

    inputs = [(0,0,0,0), (0,0,0,1), (0,1,0,1)]
    for r1, c1, r2, c2 in inputs:
        result = solution.sumRegion(r1, c1, r2, c2)
        print result

if __name__ == '__main__':
    main()
