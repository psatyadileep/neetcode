"""
understanding insertion sort
"""



def selection_sort(arr):

    for i in range(len(arr)-2):
        min = i
        for j in range(i,len(arr)):
            if arr[j]<arr[min]:
                min = j
        arr[min] , arr[i] = arr[i], arr[min]

        print(arr)
    return arr

print(insertion_sort([13,45,24,52,20,9]))

