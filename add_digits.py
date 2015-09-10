
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        return self.naive(num)

    def naive(self, n):
        result = n
        while result > 9:
            result = sum(int(s) for s in str(result))
        return result

    def congruence_formula(self, n):
        return 1 + ((n - 1) % 9)

def main():
    nums = [38]
    for n in nums:
        result = Solution().addDigits(n)
        print result

if __name__ == '__main__':
    main()
