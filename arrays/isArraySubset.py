'''
Approach:
    if an element is in hashtable/Dict
    and in a2: decrease size of a2
    if size is reduced to zero then a2 i subset
'''
def isSubset( a1, a2, n, m):
    dict={}
    for i in a1:
        if i not in dict:
            dict[i]=1
        else:
            dict[i]+=1
    for i in a2:
        if i in dict:
            m-=1
    return 'Yes'if m==0 else 'No'
# Time Complexity=O(N)
# Space Complexity=O(N)
'''
approach:
    inbuilt Method isSubset
'''
def isSubset( a1, a2, n, m):
    return 'Yes'if set(a2).issubset(set(a1)) else 'No'
# Time Complexity=O(issubset)
# Space Complexity=O(issubset)
