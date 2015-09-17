import math

def nCr(n, r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        result = [1] * (rowIndex + 1)
        if rowIndex < 2:
            return result

        # Update the array from the end to the beginning iteratively
        for i in xrange(1, rowIndex):
            for j in xrange(i, 0, -1):
                result[j] = result[j] + result[j-1]
        return result

    def binomial_coefficient(self, rowIndex):
        return [nCr(rowIndex, i) for i in xrange(rowIndex+1)]

def main():
    inputs = [0, 1, 2, 3, 4, 5]
    for n in inputs:
        result = Solution().getRow(n)
        print result

if __name__ == '__main__':
    main()
