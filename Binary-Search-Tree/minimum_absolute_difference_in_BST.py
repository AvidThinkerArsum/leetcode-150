"""
Problem: Minimum Absolute Difference in BST
LeetCode: https://leetcode.com/problems/minimum-absolute-difference-in-bst/
Difficulty: Easy
Approach: A BST arranged in order can be easily used to find such a difference between successive values. the inorder function does not need to return anything and is only there to update our variable values. 
Time: O(n) - as each node is visited once 
Space: O(h) - this depends on how much extra memory exists at the same time. and extra memory is a recursive call. so how many max recursive calls can exist at the same time and that is the depth of the tree because you keep going left. it is true that when you hit the end you will go to the right as well but then the left calls are taken off the stack and so the average max number of recursive calls you are going to have are equal to the depth. in the worst case though you might have O(n) if all the node are on one side.
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
