# There are three types of edits that can be performed on strings: insert a character, remove a character, or replace a character. Given two string, write a function to check if they are one edit or zero edits

# pale, ple -> True
# pales, pale -> True
# pale, bale -> True
# pale, bae -> False

def check_edit(length, counter):
    if length == 0:
        return length + 1 == counter
    else:
        return length == counter

def edit(str_a, str_b):
    counter = 0
    for s in str_a:
        if not s in str_b:
            counter += 1
    if check_edit(len(str_a) - len(str_b), counter):
        return True
    return False

def one_away(str_a, str_b):
    if len(str_a) > len(str_b):
        return edit(str_a, str_b)
    else:
        return edit(str_b, str_a)

    return edit(str_a, str_b)

if __name__ == '__main__':
    result = one_away('pale', 'ple')
    print(f'pale, ple -> {result}')

    result = one_away('pales', 'pale')
    print(f'pales, pale -> {result}')

    result = one_away('pale', 'bale')
    print(f'pale, bale -> {result}')

    result = one_away('pale', 'bae')
    print(f'pale, bae -> {result}')
