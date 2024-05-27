def productexceptself(arr):
    n = len(arr)
    print(n)
    print(arr)
    leftprod  = [1]*n
    rightprod = [1]*n
    result = [1]*n
    for i in range(1,n):
        leftprod[i] = leftprod[i-1] * arr[i-1]

    for i in range(n-2,-1,-1): # from n-2 to start backwards
        rightprod[i] = rightprod[i+1] * arr[i+1]   # initially right product is set to 1 for all then from second last element calculated 

    for i in range(0,n):
        result[i] = leftprod[i] * rightprod[i]
    return result

print(productexceptself([1,2,3,4,5]))