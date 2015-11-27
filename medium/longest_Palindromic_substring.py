
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        return self.longestPalindrome_2(s)

    def longestPalindrome_2(self, s):
        n = len(s)
        begin, maxlen = 0, 1
        for i in xrange(1, n):
            j = i - maxlen -1
            if j >= 0 and self.is_palindrome(s, j, i):
                begin, maxlen = j, maxlen+2
            elif self.is_palindrome(s, j+1, i):
                begin, maxlen = j+1, maxlen+1
        return s[begin:begin+maxlen]

    def longestPalindrome_1(self, s):
        # error on 'abababababababababa'
        n = len(s)
        dp = [1] * n
        end, maxlen = 0, 1
        for i in xrange(1, n):
            a = s[i]
            j = dp[i-1]
            if i-j-1 >= 0 and s[i-j-1] == a:
                dp[i] = j + 2
            elif s[i-j] == a and all(s[x]==s[x+1] for x in xrange(i-j, i)):
                dp[i] = j + 1
            elif i-2 >= 0 and s[i-2] == a:
                dp[i] = 3
            elif s[i-1] == a:
                dp[i] = 2

            if dp[i] > maxlen:
                end, maxlen = i, dp[i]

        begin = end - maxlen + 1
        return s[begin:begin+maxlen]

    def longestPalindrome_0(self, s):
        result = ''
        n = len(s)
        begin, maxlen = 0, 1
        for i in xrange(1, n):
            for j in xrange(0, i+1):
                size = i - j + 1
                if (self.is_palindrome(s, j, i) and size > maxlen):
                    begin, maxlen = j, size
        return s[begin:begin+maxlen]

    def is_palindrome(self, s, lo, hi):
        n = hi - lo + 1
        return all(s[lo+i] == s[hi-i] for i in xrange(n/2))

def main():
    inputs = ['aabcddcbab', '', 'a']
    inputs += ['abaa', 'abbaa']
    inputs += ['abababababababababa']
    for s in inputs:
        #print Solution().longestPalindrome_0(s)
        result = Solution().longestPalindrome(s)
        print result

if __name__ == '__main__':
    main()
