"""
Problem: Contains Duplicate II
LeetCode: https://leetcode.com/problems/contains-duplicate-ii/
Difficulty: Easy
Approach: Basically we use a hashmap and for each number we store its value as the last index where we saw it. Then, if a number already exists in the hashmap we check whether it has the suitable distance. if not we rewrite the new index over there which could now function as the closest.
Time: O(n)
Space: O(n)
"""

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashmap = {}
        for i in range(len(nums)):
            if nums[i] not in hashmap or (i - hashmap[nums[i]]) > k:
                hashmap[nums[i]] = i
            else:
                return True
        return False
