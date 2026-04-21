"""
Problem: Summary Ranges
LeetCode: https://leetcode.com/problems/summary-ranges/
Difficulty: Easy
Approach: so to type values into a string you put f"string {a}" where a is the variable inserted. In this case we add these to a list. We need to run a loop through the array. We note the start and the end elt for each interval and that is it.
Time: O(N) - as each elt is visitied once despite using two while loops
Space: O(N) - as in worst case the results array can have all the elts.
"""

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        i = 0
        result = []
        while i < len(nums):
            start = nums[i]
            while i + 1 < len(nums) and nums[i+1] == nums[i] + 1:
                i += 1
            end = nums[i]
            if start == end:
                result.append(f"{start}")
            else:
                result.append(f"{start}->{end}")
            i += 1
        return result
