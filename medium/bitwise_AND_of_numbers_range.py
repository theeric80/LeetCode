
class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # find the leftmost common digits of m and n
        #return self.rangeBitwiseAnd_0(m, n)
        return self.rangeBitwiseAnd_1(m, n)

    def rangeBitwiseAnd_1(self, m, n):
        while n > m:
            n &= n-1
        return n

    def rangeBitwiseAnd_0(self, m, n):
        count = 0
        while m != n:
            m >>= 1
            n >>= 1
            count += 1
        return n << count

def main():
    inputs = [[5,5], [5,7], [5,8],]
    for m, n in inputs:
        result = Solution().rangeBitwiseAnd(m, n)
        print result

if __name__ == '__main__':
    main()
