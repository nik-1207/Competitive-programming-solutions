'''
approach:
    using Dutch National Flag problem solving algorithm.
    Two pointers one is pointing at 0 and last is pointing at last of array 
    if j encounters with negative number place it t i and increase i by one 
    else decrease j by one
'''

def negativeAtOneSIde(arr):
    i=0
    j=len(arr)-1
    while(i<j):
        if arr[j]<0:
            arr[i],arr[j]=arr[j],arr[i]
            i=i+1
        else:
            j=j-1
# SPACE COMPLEXITY = O(1)
# TIME COMPLEXITY = O(n)

#################################################################################
'''
approach :
    using quick sort partioning 
    if number is greater than 0 then increase i only.
    else swap a[i] and a[j] and increase i and j both by one
'''
def rearrange(arr, n ) :
    j = 0
    for i in range(0, n) :
        if (arr[i] < 0) :
            temp = arr[i]
            arr[i] = arr[j]
            arr[j]= temp
            j = j + 1

# SPACE COMPLEXITY = O(1)
# TIME COMPLEXITY = O(n)

#################################################################################

