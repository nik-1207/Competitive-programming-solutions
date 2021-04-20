#-------------------------------------All elements in array sre distinct-------------------------------------#

# heap is not at physical level it is at conceptual level
# it is implemented over a list ,queue or any other datastructure
'''
in a heap implemented list,considering the starting index as 1, 
parent of ith element can be found at ⌊ i/2 ⌋ . 
Left child and right child of ith node is at position 2i and 2i + 1.

'''
# import heapq collection
# link to access methods   https://docs.python.org/3/library/heapq.html
# default behaviour of heapq is min heap you can turn it into maxheap by
# multiplying -1 with all elements of array
################################################################################################################################

# sorting Approach

def (arr,k):
    arr.sort()   
    print(arr[k-1]) 


# worst case O(nlogn)

#######################################################################################

# using min heap 

import heapq
def kthSmallest(self,arr, l, r, k):
    for i in range(k):
        heapq.heapify(arr)
        res=heapq.heappop(arr)
    return res

# worst case O(n+klogn)

#######################################################################################

# using max heap

# approach:
'''
1) Build a Max-Heap MH of the first k elements (arr[0] to arr[k-1]) of the given array. 
time complexity O(k)
2) For each element, after the k’th element (arr[k] to arr[n-1]), compare it with root of MH. 
    a) If the element is less than the root then make it root and call heapify for MH 
    b) Else ignore it. 
The step 2 is O((n-k)*logk)
3) Finally, root of the MH is the kth smallest element.
Time complexity of this solution is O(k + (n-k)*Logk)

'''
# python does not directly implement max heap so we multiply all element by -1 

def kthSmallest(self,arr, l, r, k):
    for i in range(len(arr)):
        arr[i]=-1*arr[i]
    # get ready for max heap by min heap
    subheap=arr[:k]
    heapq.heapify(subheap)
    for i in range(k,len(arr)):
        if subheap[0]<arr[i]: 
            subheap[0]=arr[i]
            heapq.heapify(subheap)
    return (-1*subheap[0])

# worst case O(k + (n-k)*Logk)

##########################################################################################

# QuickSelect

'''
approach :

This is an optimization over sorting method as sort method implements quick sort.
In QuickSort, we pick a pivot element, then move the pivot element to its correct position
and partition the array around it. The idea is, not to do complete quicksort,
but stop at the point where pivot itself is k’th smallest element. 
Also, not to recur for both left and right sides of pivot,
but recur for one of them according to the position of pivot. 
The worst case time complexity of this method is O(n2), 
but it works in O(n) on average.
if k is less than pivot index ,left recur else right recur
'''
# this algorithm can be epected in linear time iff the pivot selected is random 
# i.e there will be a possibility of finding kth minimum element in O(n) time complexity

def kthSmallest(arr, l, r, k):
	if (k > 0 and k <= r - l + 1):
		pos = partition(arr, l, r)
		if (pos - l == k - 1):
			return arr[pos] 
		if (pos - l > k - 1): 
			return kthSmallest(arr, l, pos - 1, k)
		return kthSmallest(arr, pos + 1, r,
							k - pos + l - 1)
def partition(arr, l, r):
	x = arr[r]
	i = l
	for j in range(l, r):
		if (arr[j] <= x):
			arr[i], arr[j] = arr[j], arr[i]
			i += 1
	arr[i], arr[r] = arr[r], arr[i]
	return i
# worst case time complexity  O(n^2), O(n) on average.

#########################################################################################


