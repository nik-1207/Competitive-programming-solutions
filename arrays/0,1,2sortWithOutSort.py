# Given an array which consists of only 0, 1 and 2.
# Sort the array without using any sorting algorithm.
'''
approach:
three pointers p0,p1,p2 pointing the possible position of 0,1 and 2 respectively
p0 at index 0 p1 at index 1 and p2 at index n-1 now if a[p1] is 0 swap it with a[p0]
and incresae p0,p1 by 1. if a[p1] is 1 then no problem increase p1 by 1 else it is obivious 
that a[p1] is 2 then swap it with p2 and decrease it with 1 .this will shift p2 providing.
# all 2 will be placed form right to left order 
# all 0 will be placed from left to right order 
# all 1 will automatically come in center
#############   THIS PROBLEM IS DERIVATIVE OF DUTCH NATIONAL FLAG PROBLEM #############
'''


def sort012(self,a,n):
    _0=0 # pointer to index 0 pointer for 0
    _1=0 # pointer to index 0 pointer for 1
    _2=n-1 # pointer to index n-1 pointer for 2
    while(_1<=_2):
        if a[_1]==0:
        a[_1],a[_0]=a[_0],a[_1]
        _1+=1
        _0+=1
        elif a[_1]==1:
            _1+=1
        else:
            a[_1],a[_2]=a[_2],a[_1]
            _2-=1
#space Complexity = O(1)
#time Complexity = O(n)

##################################################################################

# Method 2:
'''
approach : 
count 0,1 and 2 
now in thar list place all 0 ,1 and 2 together 
'''
def sort012(arr):
    l=[0,0,0]
    for i in arr:
        l[i]=l[i]+1
    for i in range(l[0]):
        arr[i]=0
    for i in range(l[0],l[1]):
        arr[i]=1
    for i in range(l[0]+l[1],l[2]):
        arr[i]=0
#space Complexity = O(1)
#time Complexity = O(n)

##################################################################################################