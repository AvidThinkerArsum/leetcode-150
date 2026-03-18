"""
Problem: Find the Index of the First Occurrence in a String
LeetCode: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
Difficulty: Easy
Approach: figure out last index that you can run for haystack. then see if there is a match else return -1
Time: O(h*n) where h is the length of the haystack and n is the length of the needle. we essentially have two loops. the outer loop is based on the length of the haystack and the inner comparison loop is based on the length of the needle.
Space: O(n) - the slicing created this string of length n each time.
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        h = len(haystack)
        n = len(needle)
        for i in range(h-n+1):
            if haystack[i:i+n] == needle:
                return i
        return -1
