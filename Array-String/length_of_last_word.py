Problem: Length of Last Word
LeetCode: https://leetcode.com/problems/length-of-last-word/
Difficulty: Easy
Approach: I can use the list function to convert a string into an array but then in this case I will have to run a for loop to find the length of the last word. Instead I can use the split command to split the string by empty space and then just use len function on the last entry. 
Time: O(n) as split has to run through the whole list. 
Space: O(n) because we have to make the new list.
Note: The space complexity can be improved to constant by using a while loop to go from right to left of the string until we reach a non empty character and the counting that sequence using a counter. This was space complexity would be O(1) and time complexity will still be O(n) and that can't be improved.
"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        a = s.split()
        return len(a[-1])
