"""
Problem: Linked List Cycle
LeetCode: https://leetcode.com/problems/linked-list-cycle/
Difficulty: Easy
Approach: So either you have a list or you don't. If you do then to check for a cycle use two pointers of different speeds and it is guaranteed that they will cross if there is a cycle. If they don't cross and you get to the end then it means you don't have a cycle. To check if they reach the end you can use the faster pointer in your conditional.
Time: O(n)
Space: O(1)
"""

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False
