"""
Problem: Valid Anagram
LeetCode: https://leetcode.com/problems/valid-anagram/
Difficulty: Easy
Approach: Make a hashmap as this question is about counts. Check for length, then check if the alphabet from the second string exists in the first. In the case of negative, return False. You will never complete the second part and get a positive remainder so no need to check for it. This is because the lengths of the two strings must be equal at that moment and so if you have a positive then you must have a negative as well which will get caught and give you False.
Time: O(n)
Space: O(n)
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freq = {}

        # Count characters in s
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        # Subtract using t
        for ch in t:
            if ch not in freq:
                return False
            freq[ch] -= 1
            if freq[ch] < 0:
                return False

        return True
