"""
Problem: Valid Sudoku
LeetCode: https://leetcode.com/problems/valid-sudoku/
Difficulty: Medium
Approach:
Time:
Space:
"""

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check rows
        for r in range (9):
            seen = set()
            for c in range (9):
                val = board[r][c]
                if val == ".":
                    continue
                elif val in seen:
                    return False
                seen.add(val)
        
        # check columns
        for c in range (9):
            seen = set()
            for r in range (9):
                val = board[r][c]
                if val == ".":
                    continue
                elif val in seen:
                    return False
                seen.add(val)

        # find 3x3 boxes
        for r in range (0, 9, 3):
            for c in range (0, 9, 3):
                seen = set()
                # check each box
                for row in range (r, r+3):
                    for col in range (c, c+3):
                        val = board[row][col]
                        if val == ".":
                            continue
                        elif val in seen:
                            return False
                        seen.add(val)

        return True                    
