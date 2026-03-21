"""
Problem: Longest Consecutive Sequence
LeetCode: https://leetcode.com/problems/longest-consecutive-sequence/
Difficulty: Easy
Approach: A runtime of O(n) is a condition we have to satisify and that should instantly tell us that we should not use sorting which usually has O(nlogn) or nested loops which have O(n^2) runtime. So, we have to use sets as lookup is O(1). Then, we must ask where do we start. Well we start from numbers that have no numbers before them. Also, a set takes out all repetitions and so that works nicely as well.
Time: O(n) for the for loop and while loop as each numbers gets walked through only once. This is interesting becase say for the given first example we start with 1 and then 2, 3, 4. now, we won't start from 2, 3, 4 again as they are not starting points and so in this way each number is visited only once.
Space: O(n) for building the set.
"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest_sequence = 0
        for num in num_set: #O(1) lookup
            if num-1 not in num_set: # starting number
                current = num
                streak = 1
                while current+1 in num_set:
                    current += 1
                    streak += 1
                longest_sequence = max(longest_sequence, streak)
        return longest_sequence
