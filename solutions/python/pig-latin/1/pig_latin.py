def translate(text):
    words = text.split()
    translated_words = []
    
    vowels = {'a', 'e', 'i', 'o', 'u'}

    for word in words:
        
        if word.startswith(('xr', 'yt')) or word[0] in vowels:
            translated_words.append(word + 'ay')
            continue

        if word.startswith('qu'):
            translated_words.append(word[2:] + 'quay')
            continue
        elif word[1:3] == 'qu':
            translated_words.append(word[3:] + word[0] + 'quay')
            continue

        lst = []
        for index, char in enumerate(word):
            if char in vowels:
                break
            if char == 'y' and index > 0:
                break
            lst.append(char)
            
        if len(lst) >= 1:
            translated_words.append(word[len(lst):] + ''.join(lst) + 'ay')
            
    return ' '.join(translated_words)