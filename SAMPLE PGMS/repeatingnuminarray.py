from typing import List




def findDuplicate(arr: List[int]) -> int:
    n = len(arr)
    arr.sort()
    for i in range(n - 1):
        if arr[i] == arr[i + 1]:
            return arr[i]


# if __name__ == "__main__":
arr = [1, 3, 4, 2, 2]  
print("The duplicate element is ", findDuplicate(arr))