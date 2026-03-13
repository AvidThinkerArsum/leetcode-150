"""
Problem: Minimum Absolute Difference in BST
LeetCode: https://leetcode.com/problems/minimum-absolute-difference-in-bst/
Difficulty: Easy
Approach: A BST arranged in order can be easily used to find such a difference between successive values. the inorder function does not need to return anything and is only there to update our variable values. 
Time: 
Space:
"""

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.prev = None
        self.min_diff = float('inf')
        self.inOrder(root)
        return self.min_diff

    def inOrder(self, root):    
        if not root:
            return
        else:
            self.inOrder(root.left)
            if self.prev is not None:
                self.min_diff = min(self.min_diff, root.val - self.prev)
            self.prev = root.val
            self.inOrder(root.right)
