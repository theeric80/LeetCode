
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0
        n = len(s)
        result = [0] * (n+1)
        result[0] = 1
        result[1] = 1 if int(s[0]) > 0 else 0
        lo, hi = 1, 26
        for i in xrange(2, n+1):
            a = int(s[i-1])
            if a > 0:
                result[i] += result[i-1]
            b = int(s[i-2])
            if b <= 0:
                continue
            b = b*10 + a
            if lo <= b <= hi:
                result[i] += result[i-2]
        return result[-1]

def main():
    inputs = ['12']
    inputs += ['12345', '', '1']
    inputs += ['0', '01', '12045']
    for s in inputs:
        result = Solution().numDecodings(s)
        print '{0} = {1}'.format(s, result)

if __name__ == '__main__':
    main()
