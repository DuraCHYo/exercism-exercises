def is_isogram(string):
    string = ''.join([x for x in string if x.isalpha()])
    if not string:
        return True
    else:
        return sorted(set(string.lower())) == sorted(string.lower())
