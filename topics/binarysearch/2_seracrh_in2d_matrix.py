"""
LC74: Search in a 2d matrix
"""



def binary_search(matrix,target):

    rows = len(matrix)
    cols = len(matrix[0])

    first , last = 0 , rows-1
    middle = (first+last)//2

    while first<=last:

        if target>matrix[middle][-1]:
            first = middle+1

        elif target<matrix[middle][0]:
            last = middle -1

        else:
            break

    if not first<=last:
        return False


    L = 0
    R =  cols-1
    row = (first+last)//2
     while L<=R:
         m = (L+R)//2

         if target> matrix[row]:
             L = m+1






