class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        mn = 101
        mx_profit = 0

        for price in prices:
            mn = min(mn, price)
            mx_profit = max(mx_profit, price - mn)
        
        return mx_profit