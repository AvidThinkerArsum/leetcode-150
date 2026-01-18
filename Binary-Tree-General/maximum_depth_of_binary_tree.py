"""
Problem: Maximum Depth of Binary Tree
LeetCode: https://leetcode.com/problems/maximum-depth-of-binary-tree/
Difficulty: Easy
Approach: Utilizing recursion. think about the depth of a node. it is 1 (its own length) + the max of the depth between its two children. okay so if a node has one or two children then we can always use this recursion. Now, what if we have 0 children? that is the base case. In that case we return 0. Also root.val can't be none for if a node exists it must have a viable value.
Time: O(n). this is because time complextiy asks that if the input gets bigger how does the number of operations my algorithm performs grow? in this question regardless of orientation of the tree, the function is called once for each node and so the number of operations grow linearly with an increase in the number of inputs.
Space: bestcase: O(logn), worstcase: O(n). this is because space complexity measures extra memory used by the alogirthm. it includes local variables but also function call stack (recursion). for this question we build a stack to record the recursion reversal and that depending on the nature of the tree can have a best or worst case scenario and the result is worst case scenario.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # if no root, the depth of this tree is 0
        if root == None:
            return 0
        else:
            left_length = self.maxDepth(root.left)
            right_length = self.maxDepth(root.right)
            return 1 + max(left_length, right_length)
