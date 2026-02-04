"""
Problem: Best Time To Buy And Sell Stock
LeetCode: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
Difficulty: Easy
Approach:
Time:
Space:

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        i = 0
        while i < len(prices) - 1:
            j = i + 1
            for k in range(j, len(prices)):
                if (prices[k] - prices[i]) > profit:
                    profit = prices[k] - prices[i]
            i += 1
        return profit
