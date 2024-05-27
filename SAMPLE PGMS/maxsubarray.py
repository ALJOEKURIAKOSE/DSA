def max_subarray_sum(arr):
    max_sum = float('-inf')  # Initialize max_sum to negative infinity
    current_sum = 0
    start_ind = 0
    end_ind = 0

    for num in arr:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum

# Example usage:
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
result = max_subarray_sum(arr)

print("Maximum Subarray Sum:", result)
# print("last", end)
# print("start", start)



# def max_subarray_sum_with_array(arr):
#     max_sum = float('-inf')  # Initialize max_sum to negative infinity
#     current_sum = 0
#     start_index = temp_start = 0
#     end_index = -1

#     for i, num in enumerate(arr):
#         if current_sum + num < num:
#             temp_start = i
#             current_sum = num
#         else:
#             current_sum += num

#         if current_sum > max_sum:
#             start_index = temp_start
#             end_index = i
#             max_sum = current_sum

#     return max_sum, arr[start_index : end_index + 1]

# # Example usage:
# arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# result_sum, result_array = max_subarray_sum_with_array(arr)
# print("Maximum Subarray Sum:", result_sum)
# print("Maximum Subarray:", result_array)

