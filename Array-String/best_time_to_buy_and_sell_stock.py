"""
Problem: Best Time To Buy And Sell Stock
LeetCode: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
Difficulty: Easy
Approach: The inital approach given at the bottom is to check all combinations but it runs out of time as it is O(n^2). The better approach is to have a min_price and a max_profit to iterate through the list.
Time: O(n)
Space: O(1)

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
