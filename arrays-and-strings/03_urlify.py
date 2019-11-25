# Write a method to replace all spaces in a string with %20

def urlify(string):
    return string.replace(' ', '%20')


if __name__ == '__main__':
    url = urlify('lorem ipsum dolor')
    print(url)
