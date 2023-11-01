# Usage of EVEN A SINGLE Float in the operation always yields a Float result
2 + 3

3462 - 3612

2368 * 4643

# Division
#  "/" represents "Standard Division"
#  "//" represents "Integer Division"
#  "%" represents "Modular Division"
#  Division by ZERO by the use of any Division Operator begets ERROR

# # Standard Division
# print(6/2 ,'\t', 7/2)
# # Always yields "Float" result

# # Integer Division
# print(6//2 ,'\t', 7//2)
# # Always returns the nearset whole number 'rounded Down'

# # Modular Division
# print(6%2 ,'\t', 7%2)
# # Always returns the remainder upon performing the mentioned division

# # Power Operator "**"
# # a**b = a^b
# print(3**3)

# "+" and "-" are binary (and also unitary) operators

# ORDER OF OPERATORS
# 1. ** (Exponents)
# 2. *  (Multiplication)
# 3. "/" , "//" , "%"  (Division(s))
# 4. +  (Addition)
# 5. -  (Subtraction)

# In py, theprecision of Floats is limited

# Exponential Exception
# In case of multiple Exponents, Start from the RIGHT (uses RIGHT-SIDED BOUNDING)
print(2 ** 2 ** 3)  # = 256 (not 64)