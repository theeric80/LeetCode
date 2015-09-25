
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and (n & (n-1)) == 0

def main():
    inputs = [0, 38, 4]
    for n in inputs:
        result = Solution().isPowerOfTwo(n)
        print result

if __name__ == '__main__':
    main()
