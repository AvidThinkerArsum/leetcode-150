"""
Problem: Find the Index of the First Occurrence in a String
LeetCode: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
Difficulty: Easy
Approach:
Time:
Space:
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        h = len(haystack)
        n = len(needle)
        for i in range(h-n+1):
            if haystack[i:i+n] == needle:
                return i
        return -1
