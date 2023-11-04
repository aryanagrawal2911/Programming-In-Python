# Given strings a and b, check if they are anagrams of each other
# Here anagrams do not necessarily need to have proper meanings

# Easy One liner Method with Counter (similar to Hashmap)
from collections import Counter

def checkAnagram(a, b):
    return Counter(a) == Counter(b)