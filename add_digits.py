
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        result = num
        while result > 9:
            result = sum(int(s) for s in str(result))
        return result

def main():
    nums = [38]
    for n in nums:
        result = Solution().addDigits(n)
        print result

if __name__ == '__main__':
    main()
