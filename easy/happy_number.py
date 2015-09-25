
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        pool = set((n,))
        x, h = n, 0
        while True:
            while x > 0:
                x, digit = divmod(x, 10)
                h += digit**2
            if h == 1:
                return True
            elif h in pool:
                return False
            else:
                #print 'unhappy number: {}'.format(h)
                pool.add(h)
                x, h = h, 0

def main():
    inputs = [19]
    for n in inputs:
        result = Solution().isHappy(n)
        print result

if __name__ == '__main__':
    main()
