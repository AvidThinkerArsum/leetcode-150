"""
Problem: Longest Common Prefix
LeetCode: https://leetcode.com/problems/longest-common-prefix/
Difficulty: Easy
Approach: This question is just looking to see what the longest common substring is given that it starts from the first index and that it is consecutive. 
Time: O(nm) - where n is the total number of elements and m is the length of the first element.
Space: O(1) - we don't create anything.
"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i in range( len ( strs[0] ) ):
            char = strs[0][i]
            for str in strs:
                if (i > len(str) - 1) or str[i] != char:
                    return strs[0][:i]
        return strs[0]
