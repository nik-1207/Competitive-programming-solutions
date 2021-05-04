'''
approach:
    recursive
'''
def fun(n):
    if n==0 or n==1:
        return 1
    else:
        return fun(n-1)*n
# time Complexity= O(N)
#SPACE COMPLEXITY = O(n)
'''
Approach:
    Iterative
'''
def fun(n):
    p=1
    for i in range(1,n+1):
        p*=i
    return p