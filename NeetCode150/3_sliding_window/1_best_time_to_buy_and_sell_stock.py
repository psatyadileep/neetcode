"""

LC:121  best time to bul and selll stok
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock
and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
"""

"""
Approach1: Brute Force 
-> have a loop1 
"""

class Solution:
    def maxProfit(self, prices) -> int:
        max_profit = float('-inf')

        for i in range(len(prices)):
            profit = 0
            for j in range(i+1,len(prices)):

                if nums[j]>num[i]:
                    profit = max(max_profit,nums[j]-nums[i])


        return  max_profit if max_profit!=float('-inf')  else 0


"""
Approach 2: 
Input: prices = [7,1,5,3,6,4]
Output: 5

-> Iterate through the array 
-> store the element that is minimum 
-> as you iterate if the value is greater then min
-> store the profit
-> save the max profit 
"""

class Solution:
    def maxProfit(self, prices) -> int:

        minimum = float('inf')
        max_profit = 0
        profit = 0
        for val in prices:
            minimum = min(val,minimum)
            if val>=minimum:
                print(val)
                profit = val - minimum
                print(profit)
                max_profit = max(max_profit,profit)

        return max_profit

print(Solution().maxProfit([7,1,5,3,6,4]))

#
# class Solution:
#     def maxProfit2(self, prices) -> int:
#
#         profit = 0
#
#         minprice = prices[0]
#         for i in range(1,len(prices)):
#
#             minprice = min(minprice,prices[i])
#             if prices[i]>minprice:
#
#                 profit = max(profit,prices[i]-minprice)
#         return profit


