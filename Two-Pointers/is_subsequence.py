"""
Problem: Is Subsequence
LeetCode: https://leetcode.com/problems/is-subsequence/
Difficulty: Easy
Approach: The understanding is that we have to go through t regardless and so that should be the main loop and you can compare that with a pointer from s. Then, you can reach a final conclusion by seeing if the whole of s was traversed. We also have to make sure that i does not get out of index with respect to s.
Time: O(n) as we have to go through the length of t
Space: O(1)
"""

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0
        while j < len(t):
            if (i < len(s)) and t[j] == s[i]:
                i += 1
            j += 1
        if i == len(s):
            return True
        else:
            return False
