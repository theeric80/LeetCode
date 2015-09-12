
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        x = n
        result = 0
        while x > 0:
            result += (x&1)
            x = x >> 1
        return result

def main():
    inputs = [11]
    for n in inputs:
        result = Solution().hammingWeight(n)
        print '{}: {}'.format(n, result)

if __name__ == '__main__':
    main()
