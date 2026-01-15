"""
Problem: Remove Duplicates from Sorted Array
LeetCode: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
Difficulty: Easy
Approach: In questions such as these there is always some manipulation you can do using two or more pointers to the array. Also, usually one of thos pointers forms part of the direct answer you return as a solution. In this problem, I utilized two pointers. The first pointer is what I call the insert position pointer. This represents the place where we can overwrite to include an element that has not been previously included. So everything to the left of this pointer is good unique stuff. The second pointer is the array traversal pointer whose job is to go through the entire list. The key here is understanding that we do not need to check all of the correct entries and we should be fine if we just check the latest good value as all the previous values are distinct anyways and cannot be repeated again as the list was sorted to begin with.
Time: O(n)
Space: O(1)
"""

Optimal Solution:

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 1 # insert position pointer
        i = 1 # array traversal pointer
        if len(nums) == 0:
            return 0
        else:
            while i < len(nums):
                if nums[i] != nums[count-1]:
                    nums[count] = nums[i]
                    count += 1
                i += 1
            return count

Sub-Optimal First solution with time complexity O(n^2) and space complexity O(n).
The fundamental issue here is that for every new element I'm thinking if I've seen this before and becaause of that I'm traversing the whole previous list in the worst case. What we know though is that the list is sorted so we don't need to compare with the entire previous list but only with the last 'good' element because everything before it is different anyways as it is sorted.

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 1 # insert position pointer
        i = 1 # array traversal pointer
        if len(nums) == 0:
            return 0
        else:
            while i < len(nums):
                if nums[i] not in nums[:count]:
                    nums[count] = nums[i]
                    count += 1
                i += 1
            return count
