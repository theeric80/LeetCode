
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # Exponentiation by squaring
        #return self.myPow_0(x, n)
        #return self.myPow_1(x, n)
        return self.myPow_2(x, n)

    def myPow_2(self, x, n):
        if n < 0:
            x = 1 / x
            n = -n

        result = 1
        while n > 0:
            if n&1:
                result *= x
            x *= x
            n >>= 1
        return result

    def myPow_1(self, x, n):
        if n < 0:
            return self.myPow_1(1/x, -n)
        elif n == 0:
            return 1
        elif n == 1:
            return x
        elif (n%2) == 0:
            return self.myPow_1(x*x, n/2)
        return x * self.myPow_1(x*x, (n-1)/2)

    def myPow_0(self, x, n):
        if n < 0:
            return self.myPow_0(1/x, -n)
        elif n == 0:
            return 1

        tmp = self.myPow_0(x, n/2)
        if (n%2) == 0:
            return tmp * tmp
        else:
            return x * tmp * tmp

def main():
    inputs = [(2.0,3), (2.0,-3),]
    for x, n in inputs:
        result = Solution().myPow(x, n)
        print x, n, result

if __name__ == '__main__':
    main()
