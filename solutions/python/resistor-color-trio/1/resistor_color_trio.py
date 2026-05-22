def label(colors):
    res = ''
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
    main_value = int(str(color_code[colors[0]]) + str(color_code[colors[1]]))
    ohms = main_value * (10 ** color_code[colors[2]])
    
    units = ["ohms", "kiloohms", "megaohms", "gigaohms"]
    
    unit_index = 0
    while ohms >= 1000 and unit_index < len(units) - 1:
        ohms //= 1000
        unit_index += 1
        
    return f"{ohms} {units[unit_index]}"