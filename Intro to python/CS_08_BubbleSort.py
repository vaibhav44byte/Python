## Bubble Sort in python 
aList = [15,6,13,22,3,52,2]
print("Original List : ",aList)

n = len(aList)

## Traverse through all list elements
for i in range(n):
    ## Last i elements are already in place
    for j in range(0, n-i-1):

        ## Traverse the list from 0 to n-i-1
        ## Swap if the element found is greater than the next element
        if aList[j] > aList[j+1]:
            aList[j], aList[j+1] = aList[j+1], aList[j]

print("List after Bubble Sort : ",aList)