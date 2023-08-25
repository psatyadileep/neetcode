"""
Given an array of values , design a data structure that can query the sum of
of a subarray of the values
"""


class PrefixSum:
    def __init__(self):
        self.prefix = []
        total = 0
        for n in nums:
            total+=n
            self.prefix.append(total)


    def rangeSum(self,left,right):
        preRight = self.prefix[Right]
        preLeft = self.prefix[Left-1] if left>0 else 0
        return (preRight-preLeft)
