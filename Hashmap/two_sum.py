"""
Problem: Two Sum
LeetCode: https://leetcode.com/problems/two-sum/
Difficulty: Easy
Approach: Hash map with subtraction
Time: O(n)
Space: O(n)
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        relationships = {}
        for i in range(len(nums)):
            if nums[i] in relationships:
                return (i, relationships[nums[i]])
            else:
                difference = target - nums[i]
                relationships[difference] = i
        
