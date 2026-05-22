import string

def rotate(text, key):
    dictionary, upper_dictionary = string.ascii_lowercase,string.ascii_uppercase
    res = ''
    if key == 0:
        print(text)
    for char in text:
        if char.isalpha():
            if char in dictionary:
                letter_index = dictionary.index(char) + key
                if letter_index >= 26:
                    letter_index = letter_index - 26
                res += f"{dictionary[letter_index]}"
            else:
                letter_index = upper_dictionary.index(char) + key
                if letter_index >= 26:
                    letter_index = letter_index - 26
                res += f"{upper_dictionary[letter_index]}"
        else:
            res += char
    return res