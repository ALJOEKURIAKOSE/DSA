def serachinrotatedsorted(arr, target):
    left = 0
    right = len(arr)-1


    while left < right:
        mid = int((left + right) /2)
        if target == arr[mid]:
            return mid
        if(arr[left] <= arr[mid]):
            if(arr[left] <= target <arr[mid]):
                right = mid -1
            else:
                left = mid +1
        else:
            if(arr[mid] < target <=arr[right]):
                left = mid +1
            else:
                right = mid -1           

    return -1


print(serachinrotatedsorted([7,8,9,1,2,3],7))        