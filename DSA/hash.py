# Initialize a string
s = "geeksforgeeks"

# Using a list to store the count of each alphabet
# by mapping the character to an index value
arr = [0] * 26

# Storing the count
for i in range(len(s)):
	arr[ord(s[i]) - ord('a')] += 1

# Search the count of the character
ch = 'e'

# Get count
print("The count of", ch, "is", arr[ord(ch) - ord('a')])
