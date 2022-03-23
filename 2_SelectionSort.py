

def selection_sort(list):
    n = len(list)
    #One by one move boundary of unsorted subarray
    for i in range(n-1):
        #  Find the minimum element in unsorted array
        #  Minimun index
        min_index = i 
        for j in range(i+1,n):
            if(list[j] < list[min_index]):
                min_index = j

        #  Swap the found minimum element with the first
        #  element
        temp = list[min_index]
        list[min_index] = list[i]
        list[i] = temp
    
    return list


#Books solution

def findSmallest(arr):
    smallest = arr[0] #Stores the smallest value
    smallest_index = 0 #Stores the index of the smallest value
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

#Sorts the array
def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        #Finds the smallest element in the
        #array, and adds it to the new array
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

print(selectionSort([5, 3, 6, 2, 10]))
print(selection_sort([5, 3, 6, 2, 10]))