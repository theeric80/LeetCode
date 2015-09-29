
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        max_profit = 0
        min_price = prices[0]
        for n in prices:
            max_profit = max(max_profit, n-min_price)
            min_price = min(min_price, n)
        return max_profit

def main():
    inputs = [(1,1,3,2,3), (1,)]
    for prices in inputs:
        result = Solution().maxProfit(prices)
        print result

if __name__ == '__main__':
    main()
