# Given a string, write a function to check if it is a permutation of a palindrome

def is_palindrome(string):
    return string == ''.join(reversed(string))

def permutations(string, step = 0):
    if step == len(string):
        s = str(''.join(string))
        if is_palindrome(s):
            print(s)

    for i in range(step, len(string)):
        string_copy = [character for character in string]
        string_copy[step], string_copy[i] = string_copy[i], string_copy[step]

        permutations(string_copy, step + 1)

if __name__ == '__main__':
    permutations('abb')
