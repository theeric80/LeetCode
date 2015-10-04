
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        return self.searchMatrix_m(matrix, target, 0, len(matrix)-1)

    def searchMatrix_m(self, matrix, target, lo, hi):
        if hi < lo:
            return False

        mid = (lo+hi) / 2
        if target < matrix[mid][0]:
            return self.searchMatrix_m(matrix, target, lo, mid-1)
        elif target > matrix[mid][-1]:
            return self.searchMatrix_m(matrix, target, mid+1, hi)
        return self.searchMatrix_n(matrix[mid], target, 0, len(matrix[mid])-1)

    def searchMatrix_n(self, row, target, lo, hi):
        if hi < lo:
            return False

        mid = (lo+hi) / 2
        if target < row[mid]:
            return self.searchMatrix_n(row, target, lo, mid-1)
        elif target > row[mid]:
            return self.searchMatrix_n(row, target, mid+1, hi)
        return True

def main():
    inputs = [([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 3)]
    inputs = [([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 51)]
    for matrix, target in inputs:
        print matrix
        result = Solution().searchMatrix(matrix, target)
        print result

if __name__ == '__main__':
    main()
