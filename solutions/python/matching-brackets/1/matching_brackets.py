def is_paired(input_string):
    stack = []
    pairs = {'}': '{', ')': '(', ']': '['}
    
    for i in input_string:
        if i in '{([':
            stack.append(i)
        elif i in pairs:
            top_element = stack.pop() if stack else None
            if top_element != pairs[i]:
                return False
                
    return len(stack) == 0