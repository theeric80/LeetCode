
class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False

        for x in (2, 3, 5):
            while num % x == 0:
                num /= x

        return num == 1

def main():
    nums = [49, -2147483648, 6, 8, 14]
    for n in nums:
        result = Solution().isUgly(n)
        print result

if __name__ == '__main__':
    main()
