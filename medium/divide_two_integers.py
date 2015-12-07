
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        minint, maxint = -2147483648, 2147483647
        # overflow
        if ((divisor == 0) or 
            (dividend == minint and divisor == -1)):
            return maxint
        elif divisor == 1:
            return dividend

        result = 0
        sign = -1 if (dividend > 0) ^ (divisor > 0) else 1
        dividend = abs(dividend)
        divisor = abs(divisor)
        while dividend >= divisor:
            r, m = divisor, 1
            while dividend >= (r<<1):
                r <<= 1
                m <<= 1
            dividend -= r
            result += m
        return result if sign > 0 else -result

def main():
    inputs = [(21,2), (0,1), (1,1)]
    inputs += [(1,-1), (-2147483648, -1)]
    for dividend, divisor in inputs:
        result = Solution().divide(dividend, divisor)
        print '{0} / {1} = {2}'.format(dividend, divisor, result)

if __name__ == '__main__':
    main()
