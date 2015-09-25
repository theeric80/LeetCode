import math

class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 0:
            return 0
        return self.trailingZeroes_1(n)

    def trailingZeroes_1(self, n):
        # 5**(k+1) > n
        k = int(math.log(n) / math.log(5))
        return sum(n / (5**i) for i in xrange(1, k+1))

    def trailingZeroes_0(self, n):
        result = 0
        denominator = 5
        while True:
            if denominator > n:
                break
            result += int(n / denominator)
            denominator *= 5
        return result

def main():
    inputs = [5, 10]
    for n in inputs:
        result = Solution().trailingZeroes(n)
        print math.factorial(n), result

if __name__ == '__main__':
    main()
