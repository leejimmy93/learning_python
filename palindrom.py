def is_palindrom_V2(s):


    # the number of char in s.
    n = len(s)
    # compare the first half of s to the reverse of the second half of s
    # omit the middle character of an odd-length string. 
    return s[:n//2] == reverse(s[n - n//2:])

def reverse(s):
         # Return a reversed version of s.
        rev = ''
        # for each character in s, add that chca to the begining of rev.
        for ch in s:
                rev = ch + rev

        return rev

