"""
Problem: Two Sum II - Input Array is Sorted
LeetCode: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
Difficulty: Medium
Approach: Hashmap is O(N) space and as we have to do constant space we cannot use them. Also, the trick is that it is sorted so we have to use pointers. Now you can use two pointers and do a double nested loop to compare all combinations and that would be the right approach if the array was unsorted and it would take O(n2) time but because it is sorted we can do better. We can use two pointers from the two opposing sides and take a sum. If the sum is smaller than the target then that means that we have to move the left pointer towards the right because that value is too small to make up the same. The right value at that point is already the largest and we cannot do any better. Same for the other case. We also know that solution does exist. 
Time: O(N) - going left to center and right to center
Space: O(1)
"""

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        while left < right:
            sum = numbers[left] + numbers[right]
            if sum > target:
                right -= 1
            elif sum < target:
                left += 1
            else:
                return (left + 1, right + 1)
