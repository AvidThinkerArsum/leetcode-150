"""
Problem: Happy Number
LeetCode: https://leetcode.com/problems/happy-number/
Difficulty: Easy
Approach: Use hast set. Use helper function for squares. The way to check for cycles is to see if a value is repeated. That is all.
Time: O(logn)
Space: O(1)
"""

class Solution:
    def isHappy(self, n: int) -> bool:
        results = set() # O(1) look up for hast set time compared to O(n) for array
        while n != 1:
            if n in results: # cycle detected
                return False
            else:
                results.add(n)
                n = self.squares(n)
        return True
    
    def squares(self, a: int) -> int:
        a = str(a)
        total = 0
        for x in a:
            c = int(x)
            total += c*c
        return total
