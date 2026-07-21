"""
Problem: Rotate Array
LeetCode: https://leetcode.com/problems/rotate-array/
Difficulty: Medium
Approach: We can basically reverse the array once and then reverse the two sections. Now, .reverse() will reverse the array in place. However, it cannot be used on a section of the array. so for example if I did nums[:k].reverse() what happens is that nums[:k] is now a new array split from the bigger one which is nums and is still intact and it is this smaller array that gets reversed. Because of this we have to use a reverse helper function to reverse the two parts within the nums array. For figuring out k we can just do a mod on k with respect to the length of the array.
Time: O(n) because total run time is 0(n) + O(k) + O(n-k) = n+k+n-k=n
Space: O(1) no new data structure created and only k, left, right used as variables.
"""

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k %= len(nums)

        def reverse(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        reverse(0, len(nums) - 1)
        reverse(0, k - 1)
        reverse(k, len(nums) - 1)
