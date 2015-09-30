
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        return self.maxProfit_0(prices)

    def maxProfit_1(self, prices):
        return sum(n-prices[i-1] for i, n in enumerate(prices[1:], 1) if n > prices[i-1])

    def maxProfit_0(self, prices):
        result = 0
        sz = len(prices)
        sz_1 = sz - 1
        i, j = 0, 0
        while i < sz:
            while j < sz_1 and prices[j+1] >= prices[j]:
                j += 1
            result += prices[j] - prices[i]
            i = j = j + 1
        return result

def main():
    inputs = [(1,1,3,2,3,4), (1,), (1,2), (2,1)]
    for prices in inputs:
        result = Solution().maxProfit(prices)
        print result

if __name__ == '__main__':
    main()
