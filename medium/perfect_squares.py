
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = [0]*(n+1)
        self.numSquares_2(n, result)
        return result[n]

    def numSquares_2(self, n, result):
        # DP, top-down
        if result[n] > 0:
            return result[n]
        elif n == 0 and n == 1 or n == 2 or n == 3:
            return n

        sqrt_n = int(n ** 0.5)
        q = n
        for i in xrange(sqrt_n, 0, -1):
            i2 = i ** 2
            q = min(q, 1 + self.numSquares_2(n-i2, result))
        result[n] = q
        return q

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
    inputs = [12, 43, 83, 6175]
    inputs = [6175]
    for n in inputs:
        result = Solution().numSquares(n)
        print result

if __name__ == '__main__':
    main()
