"""
Problem: Group Anagrams
LeetCode: https://leetcode.com/problems/group-anagrams/
Difficulty: Easy
Approach: Use a hashmap. always think about how can I unite these values so to have a common key and in this case we can order them to group them.
Time: Assume n number of words and k is the length of the longest word. Then, we have n words and for each word it takes klogk time to sort it. So total is O(nklogk)
Space: Space complexity is the amount of memory an algorithm uses as it runs. So in this case that is O(nk)
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = {}
        for word in strs:
            sort = sorted(word)
            new = "".join(sort)
            if new in dictionary:
                dictionary[new].append(word)
            else:
                dictionary[new] = [word]
        return list(dictionary.values())
