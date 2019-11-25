# Implement a method to perform basic strings compression using the counts of repeated characters. For example, the string aabccccaaa would become a2b1c4a3

def string_compression(string):
    string = string.lower()

    counter = 0
    compression = ''

    def update_compression(s):
        return f'{compression}{s}{counter + 1}'

    for i, s in enumerate(string):
        if i + 1 == len(string):
            return update_compression(s)

        if s == string[i + 1]:
            counter += 1
        else:
            compression = update_compression(s)
            counter = 0


if __name__ == '__main__':
    result = string_compression('aabccccrRrr')
    print(result)
