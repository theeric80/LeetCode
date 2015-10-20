
class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        #return self.canWinNim_0(n, True)
        return self.canWinNim_1(n, 3)

    def canWinNim_1(self, n, k):
        # The subtraction game
        return n % (k+1) > 0

    def canWinNim_0(self, n, myturn):
        if 1 <= n <= 3:
            return myturn

        return self.canWinNim_0(n-1, not myturn) or \
            self.canWinNim_0(n-2, not myturn) or \
            self.canWinNim_0(n-3, not myturn)

def main():
    nums = [4, 5, 1348820612]
    for n in nums:
        result = Solution().canWinNim(n)
        print n, result

if __name__ == '__main__':
    main()
