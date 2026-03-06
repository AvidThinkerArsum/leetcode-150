"""
Problem: Invert Binary Tree
LeetCode: https://leetcode.com/problems/invert-binary-tree/
Difficulty: Easy
Approach: Use recursion
Time: O(n) - each node is visited once
Space: O(h)
"""

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # base case
        if not root:
            return None
        
        # recursively invert left and right sub-trees
        left = self.invertTree(root.right)
        right = self.invertTree(root.left)

        root.left = left
        root.right = right

        return root
