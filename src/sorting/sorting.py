def merge_sort(arr):
    if len(arr) < 2:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    return merge(merge_sort(left), merge_sort(right))
  
def merge(left, right):
        # iterators for traversing the halves and result
    i = j = k= 0
    merged = [0] * (len(left) + len(right))
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            # The value from the left half has been used
            merged[k] = left[i]
            # Move the iterator forward
            i += 1
        else:
            merged[k] = right[j]
            j += 1
        # Move to the next slot
        k += 1

    # For all the remaining values
    while i < len(left):
        merged[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        merged[k]=right[j]
        j += 1
        k += 1
    return merged

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
#     # Your code here
#     pass


# def merge_sort_in_place(arr, l, r):
#     # Your code here
#     pass
