def maxsubarray(arr):
    orgmax = arr[0]
    maxtillnow = arr[0]

    for i in range (1,len(arr)):
        maxtillnow = max(maxtillnow+arr[i],arr[i])
        # orgmax = max(orgmax,maxtillnow)

    return maxtillnow    


print(maxsubarray([1,-4,5,7,-4,-3,2,8]))        