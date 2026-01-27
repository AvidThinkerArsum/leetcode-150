"""
Problem: Isomorphic Strings
LeetCode: https://leetcode.com/problems/isomorphic-strings/
Difficulty: Easy
Approach: I think the approach is to think of one string as the string that is being mapped to the other string. So, we can say that we want to see if s can be mapped to t. So we will initiate an empty dictionary that will act as a hashmap. Then, for each element of s we will see if it is in the hashmap. If it is then we compare that value to the value in t. If it is not in the hashmap that means it is the first time we saw it and so we will add it to the hashmap. We will also check that the two strings are the same length. Now interestingly, the question has the statement that says that 'no two characters may map to the same character'. So, if we look at the example provided then 'foo' -> 'bar' is incorrect and our system will be able to detect it but what if it was 'bar' -> 'foo' then our system will not be able to detect it. Knowing that the second is also wrong we need to check both ways by calling an extra function twice and just alternating 's' and 't' or we can check for dual pairs in the hashmap when we are adding. I will do the first approach but the second should also work.
Time: O(n) and this is because even though the two auxillary calls run one after the other they still take linear time. It is O(n) + O(n) which is O(2n) which is still O(n)
Space: this is also O(n) as what is being measured is how much space is used in any moment. As the two auxilary functions run one after the other the maximum space at a moment is the one for any one of them and that is O(n).
"""

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            return (self.issIsomorphic(s, t) and self.issIsomorphic(t, s))
    
    def issIsomorphic(self, a: str, b: str) -> bool:
        hashmap = {}
        for i in range (len(a)):
            if a[i] not in hashmap:
                hashmap[a[i]] = b[i]
            elif hashmap[a[i]] != b[i]:
                return False
        return True
