# # Limitation of input()
# # It always returns a 'String' value, even if a numerical value is entered, Python will treat it as a String value.
# # This complicates things a bit

login = input("Enter your login: ")
language = input("Enter your native language: ")

print("Your login is", login, "and you speak", language)
