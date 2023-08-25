"""

 Maximum Subarray Sum in an Array
 Given an integer array nums, find the
subarray
 with the largest sum, and return its sum.


Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6


 Assumptions:
-> if there is no array  return  None

c
Brute Force :
-> using two Loop
--> First moves through all the ements in array
-> second loop starts from the element where first loops is starting and finds the sum of all subsequent
"""


# better Approac
class Solution:
    def maxSubArray(self, nums) -> int:

        maxsum = float("-inf")

        for i in range(len(nums)):

            sum = 0

            for j in range(i, len(nums)):
                sum += nums[j]
                maxsum = max(sum, maxsum)

        return maxsum


# print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))

# Time Compleixty = O(N)^2


# Approach:  Optimal


class Solution:
    def maxSubArray2(self, nums) -> int:
        maxsum = float("-inf")

        cursum = 0
        for val in nums:
            cursum += val
            cursum = max(cursum, 0)
            maxsum = max(maxsum, cursum)

        return maxsum


print(Solution().maxSubArray2([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
