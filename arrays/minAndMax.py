
# iterative approach
# l is input list

max=l[0]
min=l[0]
def findMinAndMax():
    for i in l:
        if (i>max):
            max=i
        elif (i<min):
            min=i

# space complexity = O(1)
# time complexity = O(n)
# Comparisions =1+2(n-2)

###############################################################################################

'''
approach:

for a list if it is even then initialize
mx and mn as 0 index value and 1 index value respectively else it is odd then
initialize mx and mn as 0 and 1 index value respectively now whole list to be 
traversed is remained of even length now traverse the list in pairs  maximum 
and minimum in pairs are compared with hte mx and mn value to gt maximum and minimum
from list

'''

def getMinMax(arr):
	n = len(arr)
	if(n % 2 == 0):
		mx = max(arr[0], arr[1])
		mn = min(arr[0], arr[1])
		i = 2
	else:
		mx = mn = arr[0]
		i = 1
	while(i < n - 1):
		if arr[i] < arr[i + 1]:
			mx = max(mx, arr[i + 1])
			mn = min(mn, arr[i])
		else:
			mx = max(mx, arr[i])
			mn = min(mn, arr[i + 1])
		i += 2
	return (mx, mn)

# Time Complexity:O(n)
# Space Complexity:O(1)
# Comparisions:3*(n-1)/2 for odd n and 3n/2-2 for even n
##########################################################################################


	def getMinMax(low, high, arr):
	arr_max = arr[low]
	arr_min = arr[low]
	if low == high:
		arr_max = arr[low]
		arr_min = arr[low]
		return (arr_max, arr_min)
	else:
		mid = (low + high) //2
		arr_max1, arr_min1 = getMinMax(low, mid, arr)
		arr_max2, arr_min2 = getMinMax(mid + 1, high, arr)
	return (max(arr_max1, arr_max2), min(arr_min1, arr_min2))

# time complexity= O(n)
# space complexity = O(n)
#number of comparision=3n/2 -2 comparisons if n is a power of 2
#It does more than 3n/2 -2 comparisons if n is not a power of 2.


##########################################################################################
