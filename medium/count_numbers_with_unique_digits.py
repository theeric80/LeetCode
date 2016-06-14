
class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        used = [False] * 10
        last = 0
        return self.countNumbersWithUniqueDigits_0(n, used, last) + 1

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

def main():
    inputs = [0,1,2,3]
    for n in inputs:
        result = Solution().countNumbersWithUniqueDigits(n)
        print 'n={}, result={}'.format(n, result)

if __name__ == '__main__':
    main()
