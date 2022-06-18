#1 Sign of Product Array
def arraySign(nums):
    #Result variable initialized in 1
    result = 1
    for num in nums: #Iterate over nums
        if num == 0: #If founds a 0 then return 0 because the whole multiplication will be 0
            return 0
        result = result * num #Multiply all the numbers from nums list
    return 1 if result > 0 else -1 #If the multiplication is positive return 1 otherwise return -1

#Tests
# [-1,-2,-3,-4,3,2,1]
# [1,5,0,2,-3]
# [-1,1,-1,1,-1]
# [-1,2,-3,4,-5]
# [-1]
# [1]
# [100,-100,99,-85]

print("----------------")
print("Solution1 ArraySign")
print(arraySign([-1,-2,-3,-4,3,2,1]))
print(arraySign([1,5,0,2,-3]))
print(arraySign([-1,1,-1,1,-1]))
print(arraySign([-1,2,-3,4,-5]))
print(arraySign([-1]))
print(arraySign([1]))
print(arraySign([100,-100,99,-85]))
print("----------------")

import sys
def maxPossibleValue(value):
    maxValue = -sys.maxsize - 1
    indexes = []
    for i in range(0, len(str(value))):
        if str(value)[i] == "5":
            indexes.append(i)
    for i in range(0, len(indexes)):
        result = int(str(value)[0 : indexes[i] : ] + str(value)[indexes[i] + 1 : :])
        maxValue = result if result > maxValue else maxValue
    return 0 if maxValue == -sys.maxsize - 1 else maxValue

print("----------------")
print("Solution1 maxPossibleValue")
print(maxPossibleValue(15958))
print(maxPossibleValue(-1525))
print(maxPossibleValue(-50))
print(maxPossibleValue(0))
print(maxPossibleValue(103523451235))
print(maxPossibleValue(1005005001001))
print("----------------")