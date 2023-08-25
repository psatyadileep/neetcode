"""

"""
"""
With every iteration othe loop we are lemeinatiing half of the items
when we eleminate half the 
the length is divided by 2

n/2 -> n/2 
time compleixty = log n 
"""

def binary_search(arr,target):

    L, R = 0 , len(arr)-1

    while L<R:

        mid = (L+R)//2

        if target>arr[midd]:
            L = mid+1
        elif target<arr[mid]:
            R = mid-1
        else:
            return mid

    return -1



"""
Time Compleixty = Log N 
Space Complexity = O (1)
"""