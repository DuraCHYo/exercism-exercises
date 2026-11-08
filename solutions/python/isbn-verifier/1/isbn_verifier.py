def is_valid(isbn):
    cleaned = isbn.replace("-", "").replace(" ", "")
    
    if len(cleaned) != 10:
        return False
        
    res = 0
    for i in range(10):
        char = cleaned[i]
        
        if i == 9 and char.upper() == 'X':
            val = 10
        elif char.isdigit():
            val = int(char)
        else:
            return False
            
        res += val * (10 - i)
        
    return res % 11 == 0