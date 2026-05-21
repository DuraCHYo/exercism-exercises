def value(colors):
    color_code = {
    'black': 0,
    'brown': 1,
    'red': 2,
    'orange': 3,
    'yellow': 4,
    'green': 5,
    'blue': 6,
    'violet': 7,
    'grey': 8,
    'white': 9
    }
    lst = []
    for i in range(len(colors)):
        lst.append(str(color_code[colors[i]]))
    return int(''.join(lst[0:2]))