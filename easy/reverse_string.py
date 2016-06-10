
class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ''.join(reversed(s))

def main():
    inputs = ['hello']
    for s in inputs:
        result = Solution().reverseString(s)
        print result

if __name__ == '__main__':
    main()
