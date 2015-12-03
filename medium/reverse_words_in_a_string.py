
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join(s.split()[::-1])

def main():
    inputs = ['the sky is blue', '', 'a']
    for s in inputs:
        result = Solution().reverseWords(s)
        print '{0} = {1}'.format(s, result)

if __name__ == '__main__':
    main()
