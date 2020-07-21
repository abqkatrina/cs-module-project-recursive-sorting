# TO-DO: Implement a recursive implementation of binary search

# The three rules for a recursive function are:

# Must have a base case.
# Must change its state to move towards the base case.
# Must call itself.

def binary_search(arr, target, start, end):
    # needs to be in order -- base case
    if end >= start: 
        #define middle
        mid = (end + start) // 2
  
        # If the middle is the target, done
        if arr[mid] == target: 
            return mid 
  
        # if target is lower than mid, search from start to mid
        elif arr[mid] > target: 
            return binary_search(arr, target, start, mid - 1) 
  
        # if target is higher than mid, search from mid to end
        else: 
            return binary_search(arr, target, mid + 1, end) 
  
    else: 
        # Element is not present in the array 
        return -1
        



# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # iterative
    pass
