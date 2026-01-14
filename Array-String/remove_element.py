"""
Problem: Remove Element
LeetCode: https://leetcode.com/problems/remove-element/
Difficulty: Easy
Approach: Rather than doing a swap between the two ends and using that to count the number of non val entries we can just rewrite to the left all of the val entries and then return the count.
Time: O(n)
Space: O(n)
"""

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[count] = nums[i]
                count += 1
        return count
