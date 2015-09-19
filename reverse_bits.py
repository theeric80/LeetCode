
class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.reverseBits_0(n)

    def reverseBits_1(self, n):
        x, y = n, 0
        for i in xrange(32):
            y <<= 1
            y |= (x & 1)
            x >>= 1
        return y

    def reverseBits_0(self, n):
        x, y = n, 0
        for i in xrange(32):
            x, r = divmod(x, 2)
            y = y*2 + r
        return y

def main():
    inputs = [(43261596, 964176192),]
    for x, y in inputs:
        result = Solution().reverseBits(x)
        print x, y, result
        assert(result == y)

if __name__ == '__main__':
    main()
