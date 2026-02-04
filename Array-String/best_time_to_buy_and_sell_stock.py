"""
Problem: Best Time To Buy And Sell Stock
LeetCode: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
Difficulty: Easy
Approach:
Time:
Space:

BEST SOLUTION:

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            else:
                max_profit = max(max_profit, price - min_price)

        return max_profit


EVEN THOUGH THE FOLLOWING SOLUTION IS CORRECT. THE TIMELIMIT EXCEEDED:

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
