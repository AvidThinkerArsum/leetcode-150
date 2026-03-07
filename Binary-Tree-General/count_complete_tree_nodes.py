"""
Problem: Count Complete Tree Nodes
LeetCode: https://leetcode.com/problems/count-complete-tree-nodes/
Difficulty: Easy
Approach: pretty straightforward
Time: O(n)
Space: O(logn) - this is because we not it is complete
"""

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)
