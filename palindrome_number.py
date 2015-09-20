
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return self.isPalindrome_1(x)

    def isPalindrome_1(self, x):
        if x < 0:
            return False
        elif x == 0:
            return True

        q, y = x, 0
        while q > y:
            # q > y: reversing till half, then compare
            q, r = divmod(q, 10)
            y = y * 10 + r

        return x == y or x == y/10

    def isPalindrome_0(self, x):
        if x < 0:
            return False
        elif x == 0:
            return True

        q, y = x, 0
        while q > 0:
            q, r = divmod(q, 10)
            y = y * 10 + r

        # overflow
        return y <= 0x7fffffff and x == y 

def main():
    nums = [1, 12, 121, 1000000003, 1534236469]
    for n in nums:
        result = Solution().isPalindrome(n)
        print n, result

if __name__ == '__main__':
    main()
