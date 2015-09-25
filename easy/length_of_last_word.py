
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        return self.lengthOfLastWord_1(s)

    def lengthOfLastWord_1(self, s):
        if not s:
            return 0

        result = 0
        p = ' '
        for c in s:
            if c != ' ':
                result = 1 if p == ' ' else result + 1
            p = c
        return result

    def lengthOfLastWord_0(self, s):
        if not s:
            return 0

        i, j = -1, -1
        sz = len(s)
        for p in xrange(sz-1, -1, -1):
            if s[p] != ' ' and j < 0:
               j = p 
            if s[p] == ' ' and j >= 0:
                i = p
                break
        return j - i

def main():
    inputs = ['Hello World', 'a', 'a  ', ' a', ' ']
    for s in inputs:
        result = Solution().lengthOfLastWord(s)
        print '"{}": {}'.format(s, result)

if __name__ == '__main__':
    main()
