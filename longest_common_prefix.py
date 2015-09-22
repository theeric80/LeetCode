
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        elif len(strs) == 1:
            return strs[0]

        i = self.longestCommonPrefix_0(strs)
        return strs[0][:i+1]

    def longestCommonPrefix_0(self, strs):
        sz = len(strs)
        i = 0
        for i, s in enumerate(strs[0]):
            for j in xrange(1, sz):
                if i >= len(strs[j]):
                    return i-1
                elif strs[j][i] != strs[0][i]:
                    return i-1
        return i

def main():
    strs = ['', '']
    strs = ['a', 'aa']
    strs = ['aa', 'a']
    result = Solution().longestCommonPrefix(strs)
    print result

if __name__ == '__main__':
    main()
