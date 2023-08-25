"""
lc75:  Sort Colors
https://leetcode.com/problems/sort-colors/
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.
"""
"""
Approach1: Brute Force
-> Using merge 
time complexity = NlogN
Space Complexity = o(n)
"""

"""
Better 2: 
-> single iteration , cnt0 , cnt1 , cnt 2
-> take a count of zeroes ,1's, 2's
-> store the count in the respective varibale
-> override the arrya with 0's,1's,2's

Time COmpleixty = 2 passes O(N)+O(N)
Space COmplexity = O(1)
"""


class Solution:
    def sortColors(self, nums: List[int]) -> None:

        count0 = 0
        count1  = 0
        count2 = 0

        for val in nums:
            if val ==0:
                count0+=1
            elif val ==1:
                count11+=1
            else:
                count2+=0


        for i in range(len(nums)):
            if count0>0:
                nums[i] = 0
                count-=1
            elif count1>0:
                nums[i]= 1
                count1-=1
            else:
                nums[i]=2




"""
Approach3 : Optimized using dutch national flag technique
"""
