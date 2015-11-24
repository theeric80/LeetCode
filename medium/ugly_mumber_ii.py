
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.nthUglyNumber_1(n)

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
