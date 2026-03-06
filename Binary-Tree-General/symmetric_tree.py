"""
Problem: Symmetric Tree
LeetCode: https://leetcode.com/problems/symmetric-tree/
Difficulty: Easy
Approach: 
Time: O(n)
Space: O(h)
"""

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        else:
            return self.mirror(root.left, root.right)
        
    def mirror(self, left, right) -> bool:
        if not left and not right:
            return True
        elif not left or not right:
            return False
        else:
            return (left.val == right.val) and self.mirror(left.left, right.right) and self.mirror(left.right, right.left)
