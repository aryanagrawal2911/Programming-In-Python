# Given a string, eliminate all “b” and “ac” in the string
# Returns the filtered string

def stringFilter(st):

    a = st.split('ac')
    st = ''.join(a)
    a = st.split('b')
    st = ''.join(a)

    return st