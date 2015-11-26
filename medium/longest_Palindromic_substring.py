
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ''
        n = len(s)
        for i in xrange(1, n+1):
            for j in xrange(0, i):
                substr = s[j:i]
                if (self.is_palindrome(substr) and 
                    len(substr) > len(result)):
                    result = substr
        return result

    def is_palindrome(self, s):
        n = len(s)
        end = n - 1
        return all(s[i] == s[end-i] for i in xrange(n/2))

def main():
    inputs = ["aabcddcbab"]
    for s in inputs:
        result = Solution().longestPalindrome(s)
        print result

if __name__ == '__main__':
    main()
