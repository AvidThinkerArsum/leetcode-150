"""
Problem: Same Tree
LeetCode: https://leetcode.com/problems/same-tree/
Difficulty: Easy
Approach:
Time: O(n) - each node is visited once
Space: O(n) - worst case. O(h) - best case. I say O(h) and not O(logn) because space complexity depends on how deep the recursion goes and that will always depend on the max depth of the tree which is h. O(logn) would be the answer if we believed the tree was perfectly balanced as in that case h = logn 
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # both empty
        if p is None and q is None:
            return True
        # if different structure
        if (p is None and q is not None) or (p is not None and q is None):
            return False
        # if same structure check the value
        if p.val != q.val:
            return False
        else:
            return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))
