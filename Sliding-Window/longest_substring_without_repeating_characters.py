"""
Problem: Longest Substring Without Repeating Characters
LeetCode: https://leetcode.com/problems/longest-substring-without-repeating-characters/
Difficulty: Medium
Approach: Use two pointer and hashmaps
Time: O(N)
Space: Don't know
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        max_length = 1 # max length of substring we know at this point
        # now we at least have two points
        first = 0
        second = 1
        hashmap = {} # stores the index value of alphabets
        hashmap[s[first]] = first
        while second <= len(s) - 1:
            if s[second] not in hashmap:
                hashmap[s[second]] = second
                max_length = max(max_length, second - first + 1)
            else: # if it is in hashmap then we have a repetition and so we reached max length of this substring
                first = max(first, hashmap[s[second]] + 1)
                hashmap[s[second]] = second
                max_length = max(max_length, second - first + 1)
            second += 1
        return max_length
