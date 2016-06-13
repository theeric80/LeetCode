
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        stack, result = [], []
        coins.sort(reverse=True)
        self.coinChange_0(coins, amount, stack, result)
        return len(result) if result else -1

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

    """
    coins = [1, 2, 5]
    amount = 100
    result = Solution().coinChange(coins, amount)
    print 'coins={}, amount={}, result={}'.format(coins, amount, result)
    """

if __name__ == '__main__':
    main()
