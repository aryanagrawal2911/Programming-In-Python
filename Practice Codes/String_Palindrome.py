# # Check if a string is palindrome

# # With appropriately filtering out the special characters and keeping only alphanumeric values
# import re

# s = input()     # Take input from blank terminal
# s = re.sub(r'[^a-zA-Z0-9]', '', s)      # Filtering to keep only alphanumeric characters
# print(s == s[::-1])

# # Without any kind of filter
# s = input()
# print(s == s[::-1])

print(chr(97))