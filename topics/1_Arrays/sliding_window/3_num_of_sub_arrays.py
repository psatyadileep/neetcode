'''
LC:1343 Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold
https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/

Given an array of integers arr and two integers k and threshold, return the number of sub-arrays of size k and average greater than or equal to threshold.


Example 1:

Input: arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4
Output: 3
Explanation: Sub-arrays [2,5,5],[5,5,5] and [5,5,8] have averages 4, 5 and 6 respectively.
 All other sub-arrays of size 3 have averages less than 4 (the threshold).
Example 2:
'''



class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:

        L = 0
        R = 0
        sum = 0
        count =0
        for R in range(len(arr)):
            sum += arr[R]
            if R-L+1==k:
                if sum/k>=threshold:
                    count+=1
                sum-=arr[L]
                L+1



        return count

