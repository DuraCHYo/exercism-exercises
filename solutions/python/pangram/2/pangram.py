import string
def is_pangram(sentence):
    return set(string.ascii_lowercase) == set(([x.lower() for x in sentence if x.isalpha()])) if sentence else False