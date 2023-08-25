"""
Find the length of the longest subarray with the same value in each position

Assumptions:
-> if not array is given return 0
-> Withe a single string the value is 1


-> 4 2 2 3 3 3
Approach1: Brute Force
-> using two loops


Time Complexity =  0(N)^2
Space Complexity =
"""
def find_longest_subarray1(arr)-> int:
    max_len = 0
    if not arr:
        return 0

    for i in range(len(arr)):
        count = 1
        for j in range(i+1 , len(arr)):
            if arr[j]==arr[i]:
                print(F"J:{j},Count:{j}")
                count+=1
                max_len = max(count,max_len)
            else:
                break

    return  max_len

# print(find_longest_subarray1([4,2,2,3,3,3]))



"""
approach2 : using pointers
-> Iterate through the array 
-> if the right is not euqal to left
-> move the left to right 
-> keep the count
"""

def find_longest_subarray2(arr)-> int:

    L = 0
    count = 0
    max_len = float("-inf")

    for R in range(len(arr)):
        if arr[R] == arr[L]:
            count=R-L+1
            max_len=max(max_len,count)
        else:
            L=R
            # count = 0
    return max_len

print(find_longest_subarray2([4,2,2,3,3,3]))



