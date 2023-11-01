# # "len(String)" gives length of string
print(len('General Kenobi'))

# Keyword/Named arguements
# python functions are constructed in such a way that all Keyword Arguements MUST have default values.
# For the "end" of a PRINT function, it's Default value is "\n"(A NEW-LINE function)
# Can be changed by :- print(String, end='.')   This adds a full-stop at the end.
print('Is it too late now to say sorry', end='?')
print('Yeah')
# In the above, the output has absoltely no gaps between "sorry" and "?" and "Yeah"

# "SEP" Keyword Arguement
# Default value : SPACE character
# use : print(String , sep='{character}')
name='John'
print('Your name is',name,'Hello', sep='-')
#Above result : Your name is-John-Hello

# Both "END" and "SEP" can be used at the same time.