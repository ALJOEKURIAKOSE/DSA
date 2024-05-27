def minrotatedsortedarray(arr):
    i = 0
    left = 0
    right = len(arr)-1
    while left < right:
        mid = (left + right)//2
        if (arr[mid]>arr[right]):
            left = mid +1
        else:
            right = mid

    print(arr[left])        

minrotatedsortedarray([5,7,1,2,3])        