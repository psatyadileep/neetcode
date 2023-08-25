"""
lc:219 : Contains Duplicate2

Given an integer array nums and an integer k,
 return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

"""

# Time Complexity = O(N)

class Solution:
    def containsNearbyDuplicate2(self, nums: List[int], k: int) -> bool:
        lookup  =()
        L  = 0
        for R in range(nums):

            if nums[R] in lookup:
                return True

            lookup.add(nums[L])

            if R-L+1>k:
                lookup.remove(nums[L])
                L+=1


        return False