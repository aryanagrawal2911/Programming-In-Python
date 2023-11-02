# Simple way to Capitalize first letter of each word in a string
# Contains modification method only {No main method given}

# Using string Slicing
def convertString(str):
    
    words = str.split()     # Splits the string on every occurence of given aarguement [default case (here) : single blank space] and returns a list
    
    str = [word[0].upper() + word[1:] for word in words]    # Modifying each word with slicing
    
    return ' '.join(str)     # Returning string value after joining all modified words back to a string


# Using Concatenation
def convertString(str):

    l=str.split()

    x=''

    for i in l:

        t=i[0].capitalize()

        x+=t

        x+=i[1:]

        x+=' '

    return x