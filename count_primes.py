
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Sieve of Eratosthenes
        if n < 2:
            return 0

        sieve = [1] * n
        sz = int(n**0.5) + 1
        result = 0
        for i in xrange(2, sz):
            # i is prime
            if sieve[i] == 1:
                result += 1
                for j in xrange(i+i, n, i):
                    sieve[j] = 0

        for i in xrange(sz, n):
            if sieve[i] == 1:
                result += 1

        return result


def main():
    nums = [1, 2, 10, 1500000]
    for n in nums:
        result = Solution().countPrimes(n)
        print result

if __name__ == '__main__':
    main()
