def next_permutation(arr):
    # Find the rightmost element smaller than its next element
    i = len(arr) - 2
    while i >= 0 and arr[i] >= arr[i + 1]:
        i -= 1

    # If no such element is found, the sequence is in descending order, and it's the last permutation
    if i == -1:
        return [1,2,3]

    # Find the smallest element to the right of i and greater than arr[i]
    j = len(arr) - 1
    while arr[j] <= arr[i]:
        j -= 1

    # Swap arr[i] and arr[j]
    arr[i], arr[j] = arr[j], arr[i]

    # Reverse the elements to the right of i
    arr[i + 1:] = reversed(arr[i + 1:])

    return arr

# Example usage:
arr = [2,1,5,4,3,0,0]    # i =1 ( value 1), j = 4 ( value 3) values are exchanged (i and j ) and value after i is reversed
next_permutation_result = next_permutation(arr.copy())
print(next_permutation_result)




# [1,4,3,2,3,4,5,8,0]  i = 6 (value = 5), j = 7 ( value = 8 ) result [1,4,3,2,3,4,8,0,5]