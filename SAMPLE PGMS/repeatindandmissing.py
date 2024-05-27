from typing import List




def findDuplicate(arr: List[int]) -> int:
    n = len(arr)
    arr.sort()
    orgsum = 0
    sum = 0
    for i in range(n):
        orgsum = orgsum + i+1   # i+1 toget value of index
        print(orgsum)
        sum = sum + arr[i]
        print(sum)
    for i in range(n - 1):
        if arr[i] == arr[i + 1]:
            repeating = arr[i]            
    return repeating,(orgsum-sum)


# if __name__ == "__main__":
arr = [1, 4, 5, 8, 3,2,2,7]   
findDuplicate(arr) 
repeat,diff = findDuplicate(arr)     # 1,2,3,4,4,6  then missing is 21 - 20 + 4
print("The repeating element is ", repeat)
print("The missing element is ", diff+ repeat)

