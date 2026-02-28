"""
Problem: Remove Duplicates from Sorted Array II
LeetCode: https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
Difficulty: Easy
Approach: As all the similar elements are side by side we don't even need a hashmap and can use pointers instead.
Time: O(n)
Space: O(1)
"""

Space Complexity O(1) solution:

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)

        write = 2

        for read in range(2, len(nums)):
            if nums[read] != nums[write - 2]:
                nums[write] = nums[read]
                write += 1

        return write

Space Complexity O(n) solution:

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        hashmap = {}
        j = 0
        for i in range (len(nums)):
            if nums[i] in hashmap:
                if hashmap[nums[i]] < 2:
                    nums[j] = nums[i]
                    j += 1
                    hashmap[nums[i]] += 1
                else:
                    pass
            else:
                nums[j] = nums[i]
                j += 1
                hashmap[nums[i]] = 1
        return j
