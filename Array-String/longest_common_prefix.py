"""
Problem: Longest Common Prefix
LeetCode: https://leetcode.com/problems/longest-common-prefix/
Difficulty: Easy
Approach:
Time: 
Space: 
"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i in range( len ( strs[0] ) ):
            char = strs[0][i]
            for str in strs:
                if (i > len(str) - 1) or str[i] != char:
                    return strs[0][:i]
        return strs[0]
