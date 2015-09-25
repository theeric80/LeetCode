
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]

        result = [[1]]
        for r in xrange(1, numRows):
            row = [1]
            for i in xrange(1, r):
                row.append( result[r-1][i-1] + result[r-1][i] )
            row.append(1)
            result.append(row)
        return result

def main():
    inputs = [5]
    for n in inputs:
        result = Solution().generate(n)
        print result

if __name__ == '__main__':
    main()
