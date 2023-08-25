"""
LC217: Contains Duplicate
https://leetcode.com/problems/contains-duplicate/

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false

Assumptions:
-> If the array has no elements return False
"""
"""
Approach : Brute Force
-> start a loop i  from 0 to len(array)
-> start a second  j loop from i+1 to len(array)
-> if array[j] is equal to arra[i] return true
-> else return False

Time Complexity O(N)^2
Space compleixty = O(1)

"""
class Solution:
    def containsDuplicate1(self, nums: List[int]) -> bool:

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[j]==nums[i]:
                    return True

        return False
print(Solution().containsDuplicate1([]))
"""
Approach2 : Sorting
-> if we sort the input, the duolicates are gonna be adajcent to each other 
-> if the adjacent values are duplicates 
-> return True if not return False

Time Complexity = N logN
Space Complexity = 
"""

class Solution:
    def containsDuplicate2(self, nums: List[int]) -> bool:
        nums = sorted(nums)
        if not nums or len(nums)<2:
            return  False


        for R in range(1,len(nums)):
            if nums[R]==nums[R-1]:
                return True

        return False

print(Solution().containsDuplicate2([1,2,3,1]))
print(Solution().containsDuplicate2([1,2,3,4]))
print(Solution().containsDuplicate2([1,1,1,3,3,4,3,2,4,2]))

""""
Approach3:
[1,1,1,3,3,4,3,2,4,2]
-> create a set
-> add elements into the set as you iterate
-> return true if the element is in the set
-> if not add to set
-> return false if ietarted through all the elemnets

Time COmplexity = o(n)
Space Complexity = O(n)
"""


class Solution:
    def containsDuplicate2(self, nums: List[int]) -> bool:
        hashset = set ()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)

        return False
