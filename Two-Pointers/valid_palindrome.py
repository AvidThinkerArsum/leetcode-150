"""
Problem: Valid Palindrome
LeetCode: https://leetcode.com/problems/valid-palindrome/
Difficulty: Easy
Approach: Indexs and the isalnum function
Time: O(n)
Space: O(n)
"""

class Solution:
    def isPalindrome(self, s: str) -> bool: 
        s_low = s.lower()
        s_new = ""
        for ch in s_low:
            if ch.isalnum():
                s_new += ch
        i = 0
        j = len(s_new) - 1
        while i<j:
            if s_new[i] == s_new[j]:
                i+=1
                j-=1
            else:
                return False
        return True
