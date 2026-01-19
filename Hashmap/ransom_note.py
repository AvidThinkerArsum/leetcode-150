"""
Problem: Ransom Note
LeetCode: https://leetcode.com/problems/ransom-note/
Difficulty: Easy
Approach: Hash map with subtraction
Time: O(m+n) where m and n are the lengths of magazine and ransomNote respectively
Space: O(n) because of the hashmap that we build which in the worst case can be as long as the ransomNote itself
"""

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # make hashmap from magazine
        hashmap = {}
        for m in magazine:
            if m in hashmap:
                hashmap[m] += 1
            else:
                hashmap[m] = 1
        
        # check if you can make ransomNote:
        for r in ransomNote:
            if r in hashmap and (hashmap[r] > 0):
                hashmap[r] -= 1
            else:
                return False
        
        return True
