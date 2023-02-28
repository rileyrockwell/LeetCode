###  Arrays and Strings ###

### Two Pointers ###


import time


### Reverse String ###
def reverse_string(s):
    string = list(s)
    i, j = 0, len(string) - 1
    while i < j:
        string[i], string[j] = string[j], string[i]
        i += 1
        j -= 1
    return "".join(string)

def reverse_string_1(s):
    return s[::-1]

def is_palindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


s = ["h","e","l","l","o"]

a = time.time()
reverse_string(s)
print(reverse_string(s))
b = time.time()

c = time.time()
reverse_string_1(s)
print(reverse_string_1(s))
d = time.time()

print("Time to completion:", round(b - a, 10))
print("Time to completion:", round(d - c, 10))


#  Squares of a Sorted Array
