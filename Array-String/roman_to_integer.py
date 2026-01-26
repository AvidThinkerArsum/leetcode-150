"""
Problem: Roman To Integer
LeetCode: https://leetcode.com/problems/roman-to-integer/
Difficulty: Easy
Approach: Look there is the way where you can group stuff together in the values dictionary. That is you have 'IV' as an entry and so you have to check for it and additionally you have to check if 'i+1' exists and you also have to move the counter by 2 in that case. The other way is to notice that the only case where we have two letters together is when the first one is smaller than the second oneand whenever that is the case we can utilize that. Now 'LC' where L is lower than C could be an issue but we are only operating with legitimate roman numerals and so we need not worry about such a case. When we do encounter such a case we can just add the subtraction to the total but we would need to skip 2 indexes. Conversely, we can subtract the current one as the future one will be added and that boils down to getting the same thing done.
Time: O(n)
Space: O(1)
"""

class Solution:
    def romanToInt(self, s: str) -> int:
        values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        total = 0
        for i in range(len(s)):
            # if this is a subtractive case
            if i + 1 < len(s) and values[s[i]] < values[s[i + 1]]:
                total -= values[s[i]]
            else:
                total += values[s[i]]
        return total
