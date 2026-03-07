"""
Problem: Path Sum
LeetCode: https://leetcode.com/problems/path-sum/
Difficulty: Easy
Approach: We are considering root to leaf. A leaf has no kids. That is the edge case. If there are kids then we can either have 2 or 1 kids. In the case of 1 kid it means we must be able to handle the null case and so that becomes our first case. The third part is the recursive step.
Time: O(n)
Space: O(h)
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
