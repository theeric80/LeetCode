
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        n = len(s) + 1
        wb = [False] * n
        wb[0] = True
        for i in xrange(1, n):
            for j in xrange(i):
                if wb[j] and s[j:i] in wordDict:
                    """
                    print 'wb[{1}]={2}, s[{1}:{0}]={3}'.format(
                        i, j, wb[j], s[j:i])
                    """
                    wb[i] = True
                    break
        return wb[-1]

def main():
    inputs = [('leetcode', ['leet', 'code']),]
    for s, wordDict in inputs:
        result = Solution().wordBreak(s, wordDict)
        print '{}, {} = {}'.format(s, wordDict, result)

if __name__ == '__main__':
    main()
