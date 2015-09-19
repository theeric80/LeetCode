import math
from itertools import count

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.climbStairs_2(n)

    def climbStairs_2(self, n):
        # Dynamic Programming
        # n = [n-1] + [n-2]
        if n <= 0:
            return 0
        elif n == 1 or n == 2:
            return n

        n1, n2 = 1, 2
        for i in xrange(3, n+1):
            n0 = n2 + n1
            n1 = n2
            n2 = n0

        return n2

    def climbStairs_1(self, n):
        # Combination
        if n <= 0:
            return 0
        elif n == 1 or n == 2:
            return n

        result = 0
        for i in count(0):       
            x = n - 2*i
            if x < 0:
                break
            #print '#1: {}, $2: {}'.format(x, i)
            result += self.nCr(x+i, i)

        return result

    def climbStairs_0(self, n):
        # Recursive
        if n <= 0:
            return 0
        elif n == 1 or n == 2:
            return n

        return self.climbStairs_0(n-1) + self.climbStairs_0(n-2)

    def nCr(self, n, r):
        f = math.factorial
        return f(n) / f(r) / f(n-r)

def main():
    # 35: 14930352
    inputs = [1, 2, 3, 4, 35]
    for n in inputs:
        result = Solution().climbStairs(n)
        print result

if __name__ == '__main__':
    main()
