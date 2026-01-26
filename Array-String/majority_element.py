"""
Problem: Majority Element
LeetCode: https://leetcode.com/problems/majority-element/
Difficulty: Easy
Approach: Every time we see two different elements, we “cancel” one occurrence of each. Minority elements can cancel each other — that’s fine. Minority elements can cancel some majority elements. But since the majority appears more than half the time, there are not enough minority elements to cancel all of it.
Time: O(n)
Space: O(1)
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num
                count = 1
            elif num == candidate:
                count += 1
            else:
                count -= 1

        return candidate
