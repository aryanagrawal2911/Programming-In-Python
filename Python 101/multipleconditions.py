# we use boolean operators to somehow jion multiple conditions
ucou = input("Enter country name : ")
uage = int(input("Enter age : "))

if uage <= 25 and ucou == "Germany":
    print("Worthy of applying for German student exchange!!!")
else:
    print("unworthy")

# Others are : 
# OR
# NOT

# Priorities:
# NOT
# AND
# OR
