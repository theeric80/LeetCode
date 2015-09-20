
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = 1 if x >= 0 else -1
        q, y = abs(x), 0
        while q > 0:
            q, r = divmod(q, 10)
            y = y * 10 + r

        # overflow case
        return y * sign if y <= 0x7fffffff else 0

def main():
    nums = [123, -123, 100, 1000000003, 1534236469]
    for n in nums:
        result = Solution().reverse(n)
        print n, result

if __name__ == '__main__':
    main()
