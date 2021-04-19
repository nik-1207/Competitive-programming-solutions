# iterative approach

def reverseArray(arr):
    i=0
    l=len(arr)-1
    while(i<l):
        arr[i],arr[l]=arr[l],arr[i]
        i=i+1
        end=end+1

# time complexity O(n)
# space COmplexity O(1)

###############################################################################################

# direct approach (slicing)

def reverseArray(arr):
    return arr[::-1]

# time complexity O(n)
# space Complexity 0

##########################################################################################

# recursive approach

def reverseArray(arr,start,end):
    arr[start],arr[end]=arr[end],arr[start]
    reverseArray(arr,start+1,end+1)

# time complexity O(n)
# space COmplexity O(n)