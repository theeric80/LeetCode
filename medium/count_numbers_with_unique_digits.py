
class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        """
        used = [False] * 10
        last = 0
        return self.countNumbersWithUniqueDigits_0(n, used, last) + 1
        """
        return self.countNumbersWithUniqueDigits_2(n)

    def countNumbersWithUniqueDigits_0(self, n, used, last):
        # backtracing
        count = 1 if last != 0 else 0
        if n == 0:
            return count

        for i in xrange(10):
            if not used[i]:
                used[i] = True
                count += self.countNumbersWithUniqueDigits_0(n-1, used, i)
                used[i] = False
        return count

    def countNumbersWithUniqueDigits_1(self, n):
        # dynamic programming
        """
        i=0: 1
        i=1: 9
        i=2: 9*9
        i=3: 9*9*8
        ...
        i=n: 9*9*8*...*(11-i)   , i<=10
        """
        sz = min(n, 10)+1
        m = [1] * sz
        for i in xrange(1, sz):
            m[i] = m[i-1] + 9 * reduce(lambda a, b: a*b, [1]+range(9, 10-i, -1))
        return m[-1]

    def countNumbersWithUniqueDigits_2(self, n):
        # dynamic programming
        sz = min(n, 10)+1
        m = [9] * sz
        m[0] = 1
        for i in xrange(2, sz):
            m[i] = m[i-1] * (11-i)
        return sum(m)

def main():
    inputs = [0,1,2,3,5,10,11]
    for n in inputs:
        result = Solution().countNumbersWithUniqueDigits(n)
        print 'n={}, result={}'.format(n, result)

if __name__ == '__main__':
    main()
