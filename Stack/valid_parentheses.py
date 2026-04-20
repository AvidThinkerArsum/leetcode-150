"""
Problem: Valid Parentheses
LeetCode: https://leetcode.com/problems/valid-parentheses/
Difficulty: Easy
Approach
Time: O(n)
Space: O(n)
"""

class Solution:
    def isValid(self, s: str) -> bool:
        dictionary = {'(':')', '{':'}', '[':']'}
        stack = []
        for char in s:
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
            elif char == ')' or char == '}' or char == ']':
                if len(stack) > 0:
                    a = stack.pop()
                    if dictionary[a] != char:
                        return False
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False
