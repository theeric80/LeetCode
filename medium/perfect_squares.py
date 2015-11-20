
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        """
        result = [0]*(n+1)
        self.numSquares_3(n, result)
        return result[n]
        """
        return self.numSquares_4(n)

    def numSquares_4(self, n):
        # Lagrange's four-square theorem
        sqrt_n = int(n**0.5)
        if sqrt_n**2 == n:
            return 1

        # 4^k(8*m + 7)
        while n % 4 == 0:
            n /= 4
        if (n % 8) == 7:
            return 4

        sqrt_n = int(n**0.5)
        for i in xrange(sqrt_n, 0, -1):
            x = n - i**2
            if (int(x**0.5))**2 == x:
                return 2

        return 3

    def numSquares_3(self, n, result):
        # DP, bottom-up
        if n == 0 and n == 1 or n == 2 or n == 3:
            return n

        result[1] = 1
        for i in xrange(2, n+1):
            q = n
            for j in xrange(1, i+1):
                j2 = j**2
                if j2 > i: break
                q = min(q, 1 + result[i-j2])
            result[i] = q

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
    inputs = [12, 43, 83, 6175, 9975]
    for n in inputs:
        result = Solution().numSquares(n)
        print result

if __name__ == '__main__':
    main()
