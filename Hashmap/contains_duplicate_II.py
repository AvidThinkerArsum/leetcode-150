"""
Problem: Contains Duplicate II
LeetCode: https://leetcode.com/problems/contains-duplicate-ii/
Difficulty: Easy
Approach: Basically we use a hashmap and for each number we store its value as the last index where we saw it. Then, if a number already exists in the hashmap we check whether it has the suitable distance. if not we rewrite the new index over there which could now function as the closest.
Time:
Space:
"""
