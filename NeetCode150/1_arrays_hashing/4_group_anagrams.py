"""
LC49: Group Anagram
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.
"""

from collections import  defaultdict
# class Solution:
#     def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
#         res = defaultdict(list)
#
#         for s in strs:
#
#             count = [0]*26 #count the characters , ranges from a..... z
#
#             for c in s: # we want to map letter a to 0 , b = 1 and so on
#                 count[ord(c)-ord('a')] +=1  # a = 80  -> 0 , 80-80  # b = 81 -> 1 , 81-80
#             #res[count].append(a) # In python list cannot be keys so we chnage it to tuples as
#             res[tuple(count)].append(s)                       #tuples are non mutable
#         print(res)
#         return res.values()
#
# print(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

# Solution 2

# class Solution:
#     def groupAnagrams2(self, strs: list[str]) :
#
#         lookup = defaultdict(list)
#
#         for s in strs:
#             key = "".join(sorted(list(s)))
#             lookup[key].append(s)
#
#         return lookup
# print(Solution().groupAnagrams2(["eat","tea","tan","ate","nat","bat"]))


#solution 3


class Solution:
    def groupAnagrams3(self, strs: list[str]) :

        lookup = defaultdict(list)

        for s in strs:
            total = 0
            for c in s:
                total += ord(c)

            lookup[total].append(s)

        print(lookup)
        return [l for l in lookup.values()]

print(Solution().groupAnagrams3(["eat","tea","tan","ate","nat","bat"]))
