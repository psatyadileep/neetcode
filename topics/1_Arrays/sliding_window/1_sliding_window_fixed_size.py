"""
LC219 : Given an integer array nums and an integer k,
 return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

https://leetcode.com/problems/contains-duplicate-ii/
Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
"""

"""
Approach1 ; Brute Force
-> Have a loop L that starts from 0 to len(arr)
-> inner iterator R that starts from i+1 to min(len(arr),L+k)
-> if arr[r]== arr[L] retur True 
-> else Retun False

Time COmplexity = o(n)^2
"""
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for L in range(len(nums)):
            for R in range(i+1,min(len(nums),L+K)):

                if nums[L]== nums[R]:
                    return True

        return False


"""
Apprach 2: Optimzed




-> have an iterator that iterates through the array 
-> L = 0 R = 0 
-> add the elemnt from R into set as you iterate 
-> check if the position R is greate than our window size , if yes move  remove the element[L
-> Keep checking if the element is already in the windos size

Time Complexity = O(n)
Space COmplexity = O(1)
"""

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        window = set()
        L = 0

        for R in range(len(nums)):
            if R-L+1>k:
                window.remove(nums[L])
                L+1

            if nums[R] in window:
                return True
            window.add(nums[R])

        return False
