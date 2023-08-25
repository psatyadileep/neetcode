"""
LC209:Find the length o fthe longest subarray , with same value in each position

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray
"""
"""
Aprrach1 : using two loops
"""

class Solution:
    def minSubArrayLen1(self, target: int, nums: list[int]) -> int:
        min_sum = float("inf")
        for i in range(len(nums)):
            sum = 0
            for j in range(i,len(nums)):
                sum+=nums[j]
                if sum>=target:
                    min_sum= min(min_sum,j-i+1)

        return 0 if min_sum == float("inf") else min_sum

print(Solution().minSubArrayLen1(7,[2,3,1,2,4,3])==2)
print(Solution().minSubArrayLen1(1,[1,4,4])==1)
print(Solution().minSubArrayLen1(11,[1,1,1,1,1,1,1,1])==0)



"""
approach2 : Using two pointer technique
-> Assign the left pointer to 0 
-> use ieterator R that ieerates through the array 
-> if the nums[R] == nums[L] increment the count , save the max count 
-> else move the left pointer to R ,reduce count to zero
-> return the maxcount
"""



class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:

        sum = 0
        length = float("inf")
        L = 0
        for R in range(len(nums)):

            sum+= nums[R]

            while sum>=target:
                length = min(length,R-L+1)
                sum-=nums[L]
                L+=1

        return 0 if length == float("inf") else length

print(Solution().minSubArrayLen(7,[2,3,1,2,4,3])==2)
print(Solution().minSubArrayLen(1,[1,4,4])==1)
print(Solution().minSubArrayLen(11,[1,1,1,1,1,1,1,1])==0)


