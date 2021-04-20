"""
approach:
    iterate over array in reverse order
"""

def reverseArray(arr):
    i=0
    l=len(arr)-1
    while(i<l):
        arr[i],arr[l]=arr[l],arr[i]
        i=i+1
        end=end+1

# time complexity = O(n)
# space COmplexity = O(1)

###############################################################################################

'''
approach :
    python provides slicing also in reverse order so use it
'''
def reverseArray(arr):
    return arr[::-1]

# time complexity O(n)
# space Complexity 0

##########################################################################################

'''
approach:
    recursively swap first and last element of array and 
    continiously decreasing start and end pointer 
'''

def reverseArray(arr,start,end):
    arr[start],arr[end]=arr[end],arr[start]
    reverseArray(arr,start+1,end+1)

# time complexity O(n)
# space COmplexity O(n)