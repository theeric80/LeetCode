
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return self.strStr_0(haystack, needle)

    def strStr_0(self, haystack, needle):
        # i: backup point
        i = 0
        sz_n = len(needle)
        sz = len(haystack) - sz_n + 1
        for i in xrange(sz):
            j = 0
            for j in xrange(sz_n+1):
                if j >= sz_n:
                    return i
                if haystack[i+j] != needle[j]:
                    break
            i += 1
        return -1

def main():
    inputs = [('', ''), ('abcd', 'bc'), ('abcd', 'cc'), ('abcd', 'd')]
    for h, n in inputs:
        result = Solution().strStr(h, n)
        print result

if __name__ == '__main__':
    main()
