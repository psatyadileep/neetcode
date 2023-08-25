"""
LC238 : Product of array except itself
https://leetcode.com/problems/product-of-array-except-self/
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Input: nums = [1,2,3,4]
Output: [24,12,8,6]

1 2 3 4

prefix sum = 1 3 6 10
postfix sum = 10 9   7  4

prefix poduct = 1 2 6 24
posfix product = 4 12 24 24

Output: [24,12,8,6]


postfix prodct =24 24 12  4

Output: [24,12,8,6]
"""

