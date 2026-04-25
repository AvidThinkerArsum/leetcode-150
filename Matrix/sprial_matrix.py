"""
Problem: Spiral Matrix
LeetCode: https://leetcode.com/problems/spiral-matrix/
Difficulty: Medium
Approach: find the four borders. then thin about the general while condition. then think about moving left and how you would do it and what changes as a result. I.e. in that case the top is going to increase by 1. Going right and down can always be considered to be okay to exceute because you can expect something but when you are going left or up you need to check your condition again as it might have changed since you ran your while loop iteration. The other way to think about this is that when we are moving right we do it and then we move top down by one or increase it. At this point the relationship between top and bottom might have broken our while loop (it did not before as the while loop checked it) and so when we move left we would NOW need to check it. Same thing with moving down as right gets changed and now we need to check if the condition is true when we move up for left and right.
Time: O(N*M) as every elt is touched
Space: O(N*M) as every elt is included
"""
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # we can set boundaries
        top = 0 # 0th row
        bottom =  len(matrix) - 1 # number of rows - 1
        left = 0 # 0th col
        right = len(matrix[0]) - 1 # number of columns - 1
        result = []

        while left <= right and top <= bottom:

            # go right
            for col in range (left, right + 1):
                result.append(matrix[top][col])
            top += 1

            # go down
            for row in range (top, bottom + 1):
                result.append(matrix[row][right])
            right -= 1

            # go left
            if top <= bottom:
                for col in range (right, left - 1, -1):
                    result.append(matrix[bottom][col])
                bottom -= 1

            # go up
            if left <= right:
                for row in range (bottom, top - 1, -1):
                    result.append(matrix[row][left])
                left += 1

        return result
