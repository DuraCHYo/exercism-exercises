import string
def is_pangram(sentence):
    return sorted(set(string.ascii_lowercase)) == sorted(set(([x.lower() for x in sentence if x.isalpha()]))) if sentence else False