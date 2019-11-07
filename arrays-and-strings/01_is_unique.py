# Implement an algorithm to determine if a string has all unique characters

def all_unique_characters(string):
    chars = {}
    for c in string:
        if c in chars:
            return False
        else:
            chars[c] = True
    return True

if __name__ == '__main__':
    unique = all_unique_characters('Lorem ipsum dolor sit amet, consectetur adipiscing elit')
    print(unique)
