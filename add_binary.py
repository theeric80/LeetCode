
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if len(a) < len(b):
            d = len(b) - len(a)
            a = '0' * d + a
        elif len(a) > len(b):
            d = len(a) - len(b)
            b = '0' * d + b

        result = ''
        c = 0
        for i in xrange(len(a)-1, -1, -1):
            n1, n2 = a[i], b[i]

            # add 2 digits
            if n1 == '1' and n2 == '1':
                n = '0' if not c else '1'
                c = 1
            elif n1 == '1' or n2 == '1':
                n = '1' if not c else '0'
                c = 0 if not c else 1
            else:
                n = '0' if not c else '1'
                c = 0

            result = n + result
            #print '{}: {} + {} = {}, c={}'.format(i, n1, n2, n, c)
        if c:
            result = '1' + result
        return result

def main():
    inputs = [('10', '11'), ('1', '1'), ('11', '1'), ('1', '11')]
    for a, b in inputs:
        result = Solution().addBinary(a, b)
        print result

if __name__ == '__main__':
    main()
