def find_anagrams(word, candidates):
    target_sorted = sorted(word.lower())
    expected = []
    
    for candidate in candidates:
        if candidate.lower() == word.lower():
            continue
        if sorted(candidate.lower()) == target_sorted:
            expected.append(candidate)
            
    return expected