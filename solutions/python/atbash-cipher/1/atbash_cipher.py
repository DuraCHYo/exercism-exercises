import string
def encode(plain_text):
    symbols = str.maketrans("", "", ",.!? ")
    res = plain_text.translate(symbols)
    modified = res.lower()
    t = str.maketrans(
        string.ascii_lowercase,string.ascii_lowercase[::-1])
    ciphered = modified.translate(t)
    return ' '.join([ciphered[i:i+5] for i in range(0, len(ciphered), 5)])
def decode(ciphered_text):
    ciphered_text = ciphered_text.replace(' ','')
    t = str.maketrans(
        string.ascii_lowercase[::-1],string.ascii_lowercase)
    return ciphered_text.translate(t)