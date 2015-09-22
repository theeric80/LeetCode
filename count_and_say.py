
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        say = '1'
        for i in xrange(n-1):
            tmp = ''
            count, x = 1, say[0]
            for c in say[1:]:
                if c == x:
                    count += 1
                else:
                    tmp += '{}{}'.format(count, x)
                    count, x = 1, c
            say = tmp + '{}{}'.format(count, x)
            print '{}: {}'.format(i+2, say)
        return say


def main():
    result = Solution().countAndSay(5)
    print result

if __name__ == '__main__':
    main()
