import random

rangeOfNumbers = 30
totalUniqueNumbers = 29

boolArray = [False]*rangeOfNumbers
uniqueNumberArray = [0]*totalUniqueNumbers

for i in range(len(uniqueNumberArray)):
    isIndexFree = True
    while isIndexFree:
        tempRand = random.randrange(1, rangeOfNumbers)
        isIndexFree = boolArray[tempRand]
        if isIndexFree:
            continue
        else:
            uniqueNumberArray[i] = tempRand
            boolArray[tempRand] = True
print(uniqueNumberArray)