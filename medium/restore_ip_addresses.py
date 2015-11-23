
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
                    if all(x < 256 for x in map(int, addr)):
                        result.append('.'.join(addr))
        return result

def main():
    # ["0.10.0.10","0.100.1.0"]
    inputs = ['25525511135', '010010']
    for s in inputs:
        result = Solution().restoreIpAddresses(s)
        print result

if __name__ == '__main__':
    main()
