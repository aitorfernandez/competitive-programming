# Given two strings, write a method to decide if one is a permutation of the other

def sort(str):
    return ''.join(sorted(str))

def permutation(s, t):
    if len(s) != len(t):
        return False
    return sort(s) == sort(t)

if __name__ == '__main__':
    result = permutation('dog', 'god')
    print(result)
