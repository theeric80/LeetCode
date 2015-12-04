
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        import sys
        if dividend > sys.maxint: return sys.maxint
        result = 0
        remainder = dividend
        while remainder >= divisor:
            remainder -= divisor
            result += 1
        return result

def main():
    inputs = [(11,2), (0,1), (1,1)]
    inputs += [(1,-1)]
    for dividend, divisor in inputs:
        result = Solution().divide(dividend, divisor)
        print '{0} / {1} = {2}'.format(dividend, divisor, result)

if __name__ == '__main__':
    main()
