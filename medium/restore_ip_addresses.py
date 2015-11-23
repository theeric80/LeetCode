
class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = []
        n = len(s)
        for i in xrange(1, 4):
            for j in xrange(i+1, i+4):
                for k in xrange(j+1, j+4):
                    if n-k <= 0 or n-k > 3:
                        continue
                    addr = s[0:i], s[i:j], s[j:k], s[k:]
                    if any((int(x) > 255) or (x[0] == '0' and len(x) > 1) for x in addr):
                        continue
                    result.append('.'.join(addr))
        return result

def main():
    inputs = ['25525511135', '010010']
    for s in inputs:
        result = Solution().restoreIpAddresses(s)
        print result

if __name__ == '__main__':
    main()
