num = int(input("Enter a number "))

# def next_palindrome(number):
#     new_number = number+1
#     while True:
#         if repr(new_number) == ''.join(repr(new_number)[::-1]):
#             return new_number
#         else:
#             print('{} is not a palindrome'.format(new_number))
#             new_number += 1

import sys

def next_palindrome(number):
    new_number = number+1
    while True:
        string = str(new_number)
        l = len(string)
        m = l//2
        for i,j in zip(range(m), range(l-1, m-1, -1)):
                if string[i] != string[j]:
                    print('{} is not a palindrome'.format(new_number))
                if i==m and j==m and string[i] == string[j]:
                    return new_number
        new_number += 1

print('{} is a palindrome'.format(next_palindrome(num)))