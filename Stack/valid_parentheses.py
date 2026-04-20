"""
Problem: Valid Parentheses
LeetCode: https://leetcode.com/problems/valid-parentheses/
Difficulty: Easy
Approach: You realize you have to use a stack as it is about corresponding pairs. Next because of relationship pairing you also need to have a dictionary. Then, all the edge cases. So if opening sequence then you push (append). If closing sequence you pop. Before popping you must check if there is stuff on the stack. If none you return False. If not match then also False. If you reach the end end but there is still stuff on the stack, then also False. Only, when you reach the end and there is nothing left, do you return True. Also, the only mistake I made was in the if condition where you have to write char = character each time and not just char = char1 or char2 or char3 as that will only do comparison for chat1.
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
