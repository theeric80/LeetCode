
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        return self.searchMatrix_1(matrix, target)

    def searchMatrix_1(self, matrix, target):
        m, n = len(matrix), len(matrix[0])
        row, col = 0, n-1
        while col >= 0 and row < m:
            if target < matrix[row][col]:
                col -= 1
            elif target > matrix[row][col]:
                row += 1
            else:
                return True
        return False

    def searchMatrix_0(self, matrix, target):
        m, n = len(matrix), len(matrix[0])
        # matrix[0][j]: the first element that is greater than or equal to target
        j = self.partition(matrix[0], target, 0, n-1)
        return any(self.search(matrix, target, i, 0, m-1) for i in xrange(j+1))

    def partition(self, row, target, lo, hi):
        if hi <= lo:
            return lo

        mid = (lo+hi) / 2
        if target > row[mid]:
            return self.partition(row, target, mid+1, hi)
        elif target < row[mid]:
            return self.partition(row, target, lo, mid)
        else:
            return mid

    def search(self, matrix, target, n, lo, hi):
        if hi < lo:
            return False

        mid = (lo+hi) / 2
        if target < matrix[mid][n]:
            return self.search(matrix, target, n, lo, mid-1)
        elif target > matrix[mid][n]:
            return self.search(matrix, target, n, mid+1, hi)
        else:
            return True

def main():
    matrix, target = [[1]], 0
    matrix, target = [[1]], 1
    matrix, target = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 5
    matrix, target = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 20
    print matrix
    result = Solution().searchMatrix(matrix, target)
    print result

if __name__ == '__main__':
    main()
