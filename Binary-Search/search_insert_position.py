"""
Problem: Search Insert Position
LeetCode: https://leetcode.com/problems/search-insert-position/
Difficulty: Easy
Approach: Binary Search Tree Approach
Time: O(n)
Space: O(1)
"""

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right)//2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return left
