
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        result = []
        if not matrix:
            return result
        m, n = len(matrix), len(matrix[0])
        l, t, r, b = 0, 0, n-1, m-1
        i, j = 0, -1
        di, dj = 0, 1
        while l <= r and t <= b:
            i, j = i + di, j + dj
            val = matrix[i][j]
            result.append(val)
            if dj > 0 and j == r:
                di, dj = 1, 0
                t += 1
            elif di > 0 and i == b:
                di, dj = 0, -1
                r -= 1
            elif dj < 0 and j == l:
                di, dj = -1, 0
                b -= 1
            elif di < 0 and i == t:
                di, dj = 0, 1
                l += 1
        return result

def main():
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]
    matrix = []
    result = Solution().spiralOrder(matrix)
    print result

if __name__ == '__main__':
    main()
