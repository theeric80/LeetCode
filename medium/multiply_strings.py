
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        v1 = int(num1)
        return str(sum(v1*int(n)*10**i for i, n in enumerate(reversed(num2))))

    def _int(self, s):
        return sum(int(c)*10**i for i, c in enumerate(reversed(s)))

    def _str(self, n):
        result = ''
        while n > 0:
            n, r = divmod(n, 10)
            result = str(r) + result
        return result if result else '0'

def main():
    inputs = [['15','15']]
    for num1, num2 in inputs:
        result = Solution().multiply(num1, num2)
        print '{} x {} = {}'.format(num1, num2, result)

if __name__ == '__main__':
    main()
