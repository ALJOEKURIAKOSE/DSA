def containsDuplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
        # print(seen)
    return False

# Example usage:
nums = [1, 2, 3, ]
print(containsDuplicate(nums))  # Output: True
