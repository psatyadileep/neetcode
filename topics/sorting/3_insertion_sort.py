def insertion_sort(arr):

    for i in range(1,len(arr)):
        j = i-1

        while j>=0 and arr[j+1]<arr[j]:
            temp = []
            arr[j+1], arr[j] = arr[j], arr[j+1]
            j-=1


    return arr



print(insertion_sort([13,45,24,52,20,9]))