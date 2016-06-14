
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        """
        stack, result = [], []
        coins.sort(reverse=True)
        self.coinChange_0(coins, amount, stack, result)
        return len(result) if result else -1
        """
        return self.coinChange_1(coins, amount)

    def coinChange_0(self, coins, amount, stack, result):
        # backtracing
        if result and len(stack) >= len(result):
            return
        elif amount < 0:
            return
        elif amount == 0:
            #print stack
            result[:] = stack[:]
            return

        for x in coins:
            stack.append(x)
            self.coinChange_0(coins, amount-x, stack, result)
            stack.pop()

    def coinChange_1(self, coins, amount):
        # dynamic programming: bottom-up
        # m[i] = INT_MAX          , if cj > i
        # m[i] = min([m[i-cj] + 1), if cj <= i
        n = amount + 1
        m = [n] * n
        m[0] = 0
        for i in xrange(1, n):
            for c in coins:
                if c <= i:
                    m[i] = min(m[i-c] + 1, m[i])
        return m[-1] if m[-1] < n else -1

def main():
    dummy = Solution().coinChange([], 0)

    coins = [1, 2, 5]
    amount = 11
    result = Solution().coinChange(coins, amount)
    print 'coins={}, amount={}, result={}'.format(coins, amount, result)

    coins = [2]
    amount = 3
    result = Solution().coinChange(coins, amount)
    print 'coins={}, amount={}, result={}'.format(coins, amount, result)

    coins = [1, 2, 5]
    amount = 100
    result = Solution().coinChange(coins, amount)
    print 'coins={}, amount={}, result={}'.format(coins, amount, result)

if __name__ == '__main__':
    main()
