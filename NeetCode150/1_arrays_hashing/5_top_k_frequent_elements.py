"""
Given an integer array nums and an integer k,
return the k most frequent elements. You may return the answer in any order.
Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
"""
"""
approach1 : Using hash map
-> sort the values 
-> add the elements to the hash set 
-> return the for k keys
"""

class Solution:
    def topKFrequent1(self, nums: list[int], k: int):

        sorted_nums = sorted(nums)
        lookup = {}
        for num in sorted_nums:
            if num not in lookup:
                lookup[num]= 1
            else:
                lookup[num]+= 1

        print(lookup.keys())

        return [num for num in lookup.keys()][:k]


print(Solution().topKFrequent1([1,1,1,2,2,3],2))
