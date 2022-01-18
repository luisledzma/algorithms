# coding: utf-8
#The binary_search function takes a sorted array and an item. If the
#item is in the array, the function returns its position.
def binary_search(list,item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high)/2
        guess = list[mid]
        print(mid)
        if guess == item:
            return mid
        if guess > item:
            high = mid -1
        else:
            low = mid + 1
    return None

#Similar to the above one but without guess.
def binary_search2(list,item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high)/2
        print(mid)
        if list[mid] == item:
            return mid
        if list[mid] > item:
            high = mid -1
        else:
            low = mid + 1
    return None

# Suppose you have a sorted list of 128 names, and you’re searching
# through it using binary search. What’s the maximum number of
# steps it would take?
# R/ log2 128 = 7 || It's the oposite to 2^7

# Suppose you double the size of the list. What’s the maximum
# number of steps now?
# R/ log2 256 = 8 || It's the oposite to 2^8


binary_search2([1, 3, 5, 7, 9,10,14,15,20,25,26,27],3)

