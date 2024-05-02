# String Slicing: s[::-1] - This is a string slicing technique in Python.

# s[:] would return the entire string as is.
# s[::] allows you to specify a step. By default, the step is 1, so s[::1] would also return the entire string as is.
# s[::-1] means start from the end towards the first, taking each character. This effectively reverses the string.

def reverseString(s):
    return s[::-1]

print("Enter a string: ")
n = input().strip()
print(reverseString(n))



