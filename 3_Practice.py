#Write out the code for the earlier sum function.
def sum(list):
    if len(list) == 0:
        return 0
    else:
        list.pop + sum(list)

#Write a recursive function to count the number of items in a list.

def count(list):
    if len(list) == 0:
        return 0
    else:
        return  1 + count(list[1:])

#Find the maximum number in a list.

def max(list):
    if len(list) == 1:
        return list[0]
    else:
        m = max(list[1:])
        m if m > list[0] else list[0]

# Remember binary search from chapter 1? It’s a divide-and-conquer
# algorithm, too. Can you come up with the base case and recursive
# case for binary search?

def binary_search(arr, low, high, x):
     if high >= low:
        mid = low + (high - low) // 2
        # If element is present at the middle itself
        if arr[mid] == x:
            return mid
        # If element is smaller than mid, then it
        # can only be present in left subarray
        elif arr[mid] > x:
            return binary_search(arr, low, mid-1, x)
        # Else the element can only be present
        # in right subarray
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        # Element is not present in the array
        return -1
