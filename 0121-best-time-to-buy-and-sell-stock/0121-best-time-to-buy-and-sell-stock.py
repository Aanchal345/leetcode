class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        mini = prices[0]
        profit = 0
        for i in range(1,len(prices)):
            diff = (prices[i]-mini)
            profit = max(profit,diff)
            mini = min(mini,prices[i])
        return profit
        