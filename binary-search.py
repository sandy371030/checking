#!/usr/bin/env python3

# Binary search works only if array is sorted form. eg: [1,2,3,4,...]

def binary_search(arr, item):
    start = 0
    end = len(arr)-1

    while start <= end:
        mid = (start+end) // 2
        
        # If item is larger than mid, then it will present in right subarray so, Ignore Left Half
        if arr[mid] < item:
            start = mid + 1
        
        # If item is smaller than mid, then it will present in left subarray so, Ignore Right Half
        elif arr[mid] > item:
            end = mid - 1
        
        # If item is equal, Return it
        else:
            return mid
    return "Not Found"



def binary_search_recursive(arr, low, high, item):

    if low <= high:
        mid = (low+high) // 2
        
        if arr[mid] == item:
            return mid
        
        elif arr[mid] > item:
            return binary_search_recursive(arr, low, mid-1, item)
        
        else:
            return binary_search_recursive(arr, mid+1, high, item)

    else:
        return "Not Found"


array = [2, 5, 7, 9, 12, 16, 19, 25, 29, 35]

print(binary_search_recursive(array, 0, len(array)-1, 19))

print(binary_search(array, 19))