
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        stack, result = [], []
        self.numSquares_0(n, stack, result)
        return min(len(l) for l in result)

    def numSquares_1(self, n, stack, result):
        if n == 0:
            result.append(len(stack))
            return

        sqrt_n = int(n ** 0.5)
        for i in xrange(sqrt_n, 0, -1):
            i2 = i ** 2
            if i2 == 1:
                result.append(len(stack)+n)
                return
            stack.append(i2)
            self.numSquares_1(n-i2, stack, result)
            stack.pop()

    def numSquares_0(self, n, stack, result):
        if n == 0:
            result.append(stack[:])
            return

        sqrt_n = int(n ** 0.5)
        for i in xrange(sqrt_n, 0, -1):
            i2 = i ** 2
            if i2 == 1:
                result.append(stack[:] + [1]*n)
                return
            stack.append(i2)
            self.numSquares_0(n-i2, stack, result)
            stack.pop()

def main():
    inputs = [12, 43]
    inputs = [83]
    for n in inputs:
        result = Solution().numSquares(n)
        print result

if __name__ == '__main__':
    main()
