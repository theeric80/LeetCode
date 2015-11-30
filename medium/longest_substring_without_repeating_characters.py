
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s:
            return self.lengthOfLongestSubstring_0(s)
        return 0

    def lengthOfLongestSubstring_0(self, s):
        result = 1
        n = len(s)
        dp = [1] * n
        for i in xrange(1, n):
            c = s[i]
            j = dp[i-1]
            sub = s[i-j:i]
            dup = sub.rfind(c)
            if dup < 0:
                dp[i] = j + 1
            else:
                dp[i] = j - dup
            result = max(result, dp[i])
        return result

def main():
    inputs = ['abcabcbb', 'bbbbb', '', 'c', 'dvdf']
    inputs = ['dvdf']
    for s in inputs:
        result = Solution().lengthOfLongestSubstring(s)
        print result

if __name__ == '__main__':
    main()
