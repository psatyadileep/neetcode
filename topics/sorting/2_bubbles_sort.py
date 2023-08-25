"""
understanding bubble sort
"""




def bubble_sort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n - 1):
        print(i)
        # Last i elements are already in place
        for j in range(n - i - 1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr
print(bubble_sort([13,45,24,52,20,9]))
