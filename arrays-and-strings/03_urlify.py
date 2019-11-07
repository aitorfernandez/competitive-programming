# Write a method to replace all spaces in a string with %20

def urlify(s):
    return s.replace(' ', '%20')

if __name__ == '__main__':
    url = urlify('lorem ipsum dolor')
    print(url)
