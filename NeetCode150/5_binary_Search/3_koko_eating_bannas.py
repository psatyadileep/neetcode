""""
LC875 :https://leetcode.com/problems/koko-eating-bananas/

Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

xample 1:

Input: piles = [3,6,7,11], h = 8
Output: 4
Example 2:

Input: piles = [30,11,23,4,20], h = 5
Output: 30


Observations:
-> The numbers hrs >= to len(pile)
-> the maximum if the largest element on th array


Approach 1: Brute force using the range from 1 - to max number in array and check
"""


class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        ans = float("inf")
        for i in range(1,max(piles)+1):

            hrs = 0
            for val in piles:
                if val%i==0:
                    hrs += val/i
                else:
                    hrs += (val//i)+1
            if hrs==h:
                return i

        return -1




print(Solution().minEatingSpeed(piles=[30,11,23,4,20], h = 5)==30)
print(Solution().minEatingSpeed([3,6,7,11], h = 8)==4)
print(Solution().minEatingSpeed([30,11,23,4,20], h = 6)==23)

# [1,2,3,4,5,6,6,7,8,9,10,11] h = 6

"""
Approach 2 : using Binary search 
-> find the max  elemnt in the array -> takes o(n) time
-> take the range from 1 to max and use the binary to  move between the array
-> if the mid take more time than the target move to the right
-> else to the left 
"""

class Solution:
    def minEatingSpeed2(self, piles: list[int], h: int) -> int:
        l = 1
        r = max(piles)


        while l<=r:
            mid = (l+r)//2

            total_hrs = 0
            for val in piles:
                if val<mid:
                    total_hrs+=1
                else:
                    if val%mid==0:
                        total_hrs += val/mid
                    else:
                        total_hrs += val//mid+1

            if total_hrs< h:
                r = mid-1
            elif total_hrs>h:
                l = mid+1
            else:
                return mid

print(Solution().minEatingSpeed2(piles=[30, 11, 23, 4, 20], h=5) == 30)
print(Solution().minEatingSpeed2([3, 6, 7, 11], h=8) == 4)
print(Solution().minEatingSpeed2([30, 11, 23, 4, 20], h=6) == 23)