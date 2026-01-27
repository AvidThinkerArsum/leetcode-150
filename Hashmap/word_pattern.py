"""
Problem: Word Pattern
LeetCode: https://leetcode.com/problems/word-pattern/
Difficulty: Easy
Approach: Same approach as the Isomorphic Strings question under the Hashmap category. It is the same exact question except that we need to use the split command on 's' to make it a list of words. We can use a type agnostic helper function where we don't specify the type for 'a' and 'b' and that would have worked as well but I choose to be cautious and defensive. Also, split commad splits the string at the empty spaces. If you want each character of a string to be a separate element in the array then you have to use the list command.
Time: O(n)
Space: O(n)
"""

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        if len(s) != len(pattern):
            return False
        else:
            return (self.issWordPattern(s, pattern) and self.isWordPattern(pattern, s))
    
    def isWordPattern(self, a: str, b: list) -> bool:
        hashmap = {}
        for i in range (len(a)):
            if a[i] not in hashmap:
                hashmap[a[i]] = b[i]
            elif hashmap[a[i]] != b[i]:
                return False
        return True

    def issWordPattern(self, a: list, b: str) -> bool:
        hashmap = {}
        for i in range (len(a)):
            if a[i] not in hashmap:
                hashmap[a[i]] = b[i]
            elif hashmap[a[i]] != b[i]:
                return False
        return True
