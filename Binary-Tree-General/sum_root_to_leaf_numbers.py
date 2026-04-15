Problem: Sum Root to Leaf Numbers
LeetCode: https://leetcode.com/problems/sum-root-to-leaf-numbers/
Difficulty: Medium
Approach: figure out how to add numbers without concatenating. use helper function. there were edge cases involved. be careful not to think of empty nodes as a path as they are not a path.
Time: O(N) - visit all nodes
Space: O(H) for recursion stack
"""

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        if not root.left and not root.right:
            return root.val

        return self.pathFinder(root.left, root.val) + self.pathFinder(root.right, root.val)

    def pathFinder(self, node, current_number: int) -> int:
        if not node:
            return 0
        else:
            current_number = (current_number * 10) + node.val
        if not node.left and not node.right:
            return current_number
        else:
            return self.pathFinder(node.left, current_number) + self.pathFinder(node.right, current_number)
