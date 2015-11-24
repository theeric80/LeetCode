
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.nthUglyNumber_2(n)

    def nthUglyNumber_2(self, n):
        result = [1]
        i2, i3, i5 = 0, 0, 0
        for i in xrange(1, n):
            u2 = 2 * result[i2]
            u3 = 3 * result[i3]
            u5 = 5 * result[i5]
            umin = min((u2, u3, u5))

            if umin == u2:
                i2 += 1
            if umin == u3:
                i3 += 1
            if umin == u5:
                i5 += 1
            result.append(umin)

        return result[-1]

    def nthUglyNumber_1(self, n):
        S = set([1, 2, 3, 5])
        def is_ugly(n):
            if n < 1:
                return False
            elif n == 1:
                return True

            for p in (2, 3, 5):
                if n % p == 0:
                    return n/p in S
            return False

        result, size, i = 1, 1, 1
        while size < n:
            i += 1
            if is_ugly(i):
                S.add(i)
                size += 1
                result = i
        return result

    def nthUglyNumber_0(self, n):
        def is_ugly(n):
            if n < 1:
                return False
            elif n == 1:
                return True

            for p in (2, 3, 5):
                while n % p == 0:
                    n /= p
            return n == 1

        result, i = [1], 1
        while len(result) < n:
            i += 1
            if is_ugly(i):
                result.append(i)
        return result[-1]


def main():
    inputs = [10, 291]
    for n in inputs:
        result = Solution().nthUglyNumber(n)
        print result

if __name__ == '__main__':
    main()
