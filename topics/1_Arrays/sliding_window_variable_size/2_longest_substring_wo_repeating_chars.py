"""
LC3:https://leetcode.com/problems/longest-substring-without-repeating-characters/
Given a string s, find the length of the longest
substring
without repeating characters.

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

"""
"""
Approch1 : two pointers
-> have a set that stores unique elements
->iterate throough the array and check if the element in resent in the array
-> if yes , pop the left elemnet from set
-> move the left pointer
-> keepe moving the right pointer
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique_elements = set()
        L = 0
        length = 0
        for R in range(len(s)):

            if s[R] in unique_elements:
                unique_elements.remove(s[L])
                L+=1

            unique_elements.add(s[R])
            length = max(length,R-L+1)


        return  length


