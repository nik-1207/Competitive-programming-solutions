'''
approach:
bruteforce 
find all possible subarray
return the sub array whose sum is maximum
'''
    def maxSubArraySum(self,A,n):
        l=[]
        def printSubArrays(arr, start, end):
            if end == len(arr):
                return
            elif start > end:
                return printSubArrays(arr, 0, end + 1)
            else:
                l.append(arr[start:end + 1])
                return printSubArrays(arr, start + 1, end)
                
        printSubArrays(A,0,0)
        maxsum=0
        for i in l:
            if sum(i)>maxsum:
                maxsum=sum(i)
        return maxsum


#worst case time complexity=O(N^2)
#WORST CASE COMPLEXITY=O(2^N)
########################################################
'''
approach:
    kadane's algorithm
    according to kadane algorithm, if the sum till now is >0
    include it in max sum else if the sum till now <0 start summing again new
    sub array and when this sum of new array will become > max sum
    replace max sum with current sum and so on ...
'''
def maxSubArraySum(self,a,size):
        maxsum=0
        currentsum=0
        for i in range(0,size):
            currentsum+=a[i]
            if currentsum>maxsum:
                maxsum=currentsum
            if currentsum<0:
                currentsum=0
        return maxsum
# TIME COMPLEXITY=O(N)
# SPACE COMPLEXITY= O(1)
###############################################