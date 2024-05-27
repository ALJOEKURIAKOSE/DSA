# def twosum(arr, target):
#     for i in range(len(arr)):
#         for j in range(len(arr)): 
#             if (arr[i] + arr[j] == target):
#                 return "YES", arr[i],arr[j]
            
# arr = [1,2,4,5,6,7]
# targetvalue = 11
# res,no1,no2 = twosum(arr,targetvalue)
# print("values are",no1,no2)


# using two pointer below

def two_sum(nums, target):
  """
  Finds two numbers in a sorted array that add up to the target sum.

  Args:
      nums: A sorted list of integers.
      target: The target sum.

  Returns:
      A list containing the indices of the two numbers, or an empty list if not found.
  """
  left, right = 0, len(nums) - 1
  while left < right:
    current_sum = nums[left] + nums[right]
    if current_sum == target:
      return [left, right]
    elif current_sum < target:
      left += 1
    else:
      right -= 1
  return []

# Example usage
nums = [2, 7, 11, 15]
# x = sorted(nums) # for storing sorted to another variable 
# nums.sort() # sort and save in the same variable


target =26
result = two_sum(nums, target)
print(result) # Output: [0, 1]