
class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        L = 0
        high_num = float("-inf")
        result = []

        for R in range(len(nums)):

            high_num = max(high_num,nums[R])


            if R-L+1>=k:
                print(f'{nums[L:R+1]},{high_num}')
                result.append(high_num)
                high_num = float("-inf")
                L+=1


        return result

print(Solution().maxSlidingWindow([1,3,-1,-3,5,3,6,7],3))

