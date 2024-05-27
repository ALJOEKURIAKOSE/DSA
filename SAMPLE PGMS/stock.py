def maxProfit(arr):
    maxPro = 0
    minPrice = float('inf')
    for i in range(len(arr)):
        minPrice = min(minPrice, arr[i])    
    
        maxPro = max(maxPro, arr[i] - minPrice)
        print(i,minPrice,maxPro)
    return maxPro

arr = [7, 4, 5, 3, 6, 4,9,5,1,8]
maxPro = maxProfit(arr)
print("Max profit is:", maxPro)
