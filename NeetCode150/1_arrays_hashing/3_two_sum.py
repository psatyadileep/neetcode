"""
LC1 : two Sum
https://leetcode.com/problems/two-sum/

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Assumptions
-> if there is no array : return -1 -1
-> if their is no target values return -1 -1

Approach1:  Brute Force
-> Create a loop i iterate from 0 to len(nums):
-> create a scond loop j iterate from i+1 to len(nums):
-> if i + j = target return the i and j
"""

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+ nums[j] == target:
                    return [i,j]


        return [-1,-1]

#
# print(Solution().twoSum([2,7,11,15],9)== [0,1])
# print(Solution().twoSum([3,2,4],6)==[1,2])
# print(Solution().twoSum([3,3],6)==[0,1])


"""
Approach2 : Optimized 

Input: nums = [2,7,11,15], target = 9

->using the two pointer technique
-> sort the element in the ascending order
-> assign left pointer t 0 , right pointer to end of the array
-> if nums[L]+nums[R]<target incerment L
-> elfi nums[L]+nums[R]>target decrement R
-> else return the indexes

Time Complexitu = N log(N)
"""


class Solution:
    def twoSum2(self, nums: list[int], target: int) -> list[int]:
        L = 0
        R = len(nums)-1
        hash_map = {}
        for key, val  in enumerate(nums):
            print(key,val)
            hash_map[val] = key
        print(hash_map)
        nums = sorted(nums)

        while L<R:
            if nums[L]+nums[R]<target:
                L+=1
            elif  nums[L]+nums[R]>target:
                R-=1
            else:
                # l = nums[L]
                # r = nums[R]
                # return [hash_map[l],hash_map[r]]
                return [hash_map[nums[L]],hash_map[nums[R]]]

# print(Solution().twoSum2([2, 7, 11, 15], 9))
# print(Solution().twoSum2([3, 2, 4], 6))
# print(Solution().twoSum2([3, 3], 6))
#

"""
Approach 3 :
Time Complexity = O (N)
Space Complexity = O(N)

"""\
""
class Solution:
    def twoSum3(self, nums: list[int], target: int) -> list[int]:
        hash_map= {}

        for key  , val in enumerate(nums):

            if target - val not in hash_map:
                hash_map[val] = key
            else:
                return [hash_map[target - val],key]



print(Solution().twoSum3([2, 7, 11, 15], 9))
print(Solution().twoSum3([3, 2, 4], 6))
print(Solution().twoSum3([3, 3], 6))



