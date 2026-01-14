"""
Problem: Two Sum
LeetCode: https://leetcode.com/problems/merge-sorted-array/
Difficulty: Easy
Approach: Utilizing three pointers
Time: O(m+n)
Space: O(1)
"""

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m-1
        j = n-1
        k = n+m-1
        while i>=0 or j>=0: # while there remains something to be explored in any of the arrays
            if j<0: # second array finished
                nums1[k] = nums1[i]
                i = i-1
            elif i<0: # first array finished
                nums1[k] = nums2[j]
                j = j-1
            elif nums1[i] >= nums2[j]: # if the el of the first array >= el of second array
                nums1[k] = nums1[i]  # write down that el at the end of the first array
                i = i-1 # move i one left
            else: # if the el of the second array >= el of the first array
                nums1[k] = nums2[j] # write down that el at the end of the first array
                j = j-1 # move j one left
            k = k-1 # last spot is now taken, move k left
            
