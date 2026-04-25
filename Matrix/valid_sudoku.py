"""
Problem: Valid Sudoku
LeetCode: https://leetcode.com/problems/valid-sudoku/
Difficulty: Medium
Approach: Handle each condition. Matrix question will rely on use intelligent and precise looping.
Time: O(N^2) - The row check finished first and then the column check starts. They don't run at the same time which is why we add them. Now, for one of them we have 9x9 so N^2
Space: O(N). Again at a single moment only one of our three main checks is running as they don't run in paralell. Now, it is the same set being used over and over. Take the example of the row check. The max size of the set is 9 and for each row we can make a new set and so space complexity which is the max space used at any one point is going to be O(N)
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
