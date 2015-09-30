
class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = [0]
        for i in xrange(0, n):
            x = 2**i
            # 1) reverse the result list from i-1 bit
            # 2) prefix the reversed items with '1'
            result.extend(x+y for y in result[::-1])
        return result

def main():
    inputs = [2, 0, 1, 3]
    for n in inputs:
        result = Solution().grayCode(n)
        print result

if __name__ == '__main__':
    main()
