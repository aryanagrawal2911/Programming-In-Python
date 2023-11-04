# Given a string containing only lowercase characters, replace accordingly :
# If the alphabet is a vowel, replace it with its next letter in the lexographical order,
# But in case of a consonant, replace it with its previous letter in the lexographical order

def encodeString(s: str, n: int) -> str:
	
    sv = 'aeiou'
    r = ''

    for i in s:

        if i in sv:
            r += chr(ord(i) + 1)

        else:
            r += chr(ord(i) - 1)

    return r