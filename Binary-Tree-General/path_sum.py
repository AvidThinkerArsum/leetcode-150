"""
Problem: Path Sum
LeetCode: https://leetcode.com/problems/path-sum/
Difficulty: Easy
Approach:
Time:
Space:
"""

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # no chance
        if not root:
            return False
        # is a leaf
        targetSum -= root.val
        if not root.left and not root.right and targetSum == 0:
            return True
        else:
            return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)
