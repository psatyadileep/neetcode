"""
lc242: Valid Anagram
https://leetcode.com/problems/valid-anagram/

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.


Assumptions:
-> is one the strings is not give return False

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false


Approach1: Optimal

-> create a hash map
-> store the letters as key with their frquency of repetition
-> iterate through the second word and check of the key is present with frequcny >0
-> if not return False

"""



class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_map = {}
        count= 0
        for letter in s:

            if letter not in hash_map:
                hash_map[letter]= 1
            else:
                hash_map[letter]+=1
            count+=1

        for letter in t:
            if letter in hash_map and  hash_map[letter]>0:
                hash_map[letter]-= 1
                count-=1
            else:
                return False
        return True if not count else False


"""
Approach2 
-> calculate length of s and T if not same return False
-> create 2 hashmaps one for S and one for T with the character frequncies
-> iterate the through the hashmaps and see that the frequcnies
are same for the letters
-> if not return false else return True  if the loop exits
"""

"""
Aprpoach 2 : using counter 
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        return counter(s)==counter(t)