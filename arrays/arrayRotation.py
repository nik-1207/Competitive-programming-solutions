'''
approach: 
    Input arr[] = [1, 2, 3, 4, 5, 6, 7], d = 2, n =7
    1) Store d elements in a temp array
    temp[] = [1, 2]
    2)left Shift rest of the arr[]
    arr[] = [3, 4, 5, 6, 7, 6, 7]
    3) Store back the d elements at end
    arr[] = [3, 4, 5, 6, 7, 1, 2]
'''
def rotateArray(arr, n, d):
    temp = []
    i = 0
    while (i < d):
        temp.append(arr[i])
        i = i + 1
    i = 0
    while (d < n):
        arr[i] = arr[d]
        i = i + 1
        d = d + 1
    arr[:] = arr[: i] + temp
    return arr  
# SPACE  COMPLEXITY = O(d)
# TIME COMPLEXITY = O(n)
##############################################################
'''
approach:
    rotate the list by one d times 
'''
def leftRotate(arr, d, n):
    for i in range(d):
        temp = arr[0]
    for i in range(n-1):
        arr[i] = arr[i+1]
    arr[n-1] = temp
# TIME COMPLEXITY = O(d*n)
# SPACE COMPLEXITY = O(1)
######################################################################
'''
approach :
    JUGGLING ALGORITHM
    Instead of moving one by one, divide the array in different sets 
    where number of sets is equal to GCD of n and d.
    And move the elements within sets. If GCD is 1 then elements will be moved within one set only
    we just start with temp = arr[0] and keep moving arr[I+d] to arr[I] 
    and finally store temp at the right place.
'''
def leftRotate(arr, d, n):
    d = d % n
    g_c_d = gcd(d, n)
    for i in range(g_c_d):
        temp = arr[i]
        j = i
        while 1:
            k = j + d
            if k >= n:
                k = k - n
            if k == i:
                break
            arr[j] = arr[k]
            j = k
        arr[j] = temp
######################################################################
'''
approach :
    using list slicing

'''
def rotateList(arr,d,n):
  arr[:]=arr[d:n]+arr[0:d]
  return arr
#######################################################################################