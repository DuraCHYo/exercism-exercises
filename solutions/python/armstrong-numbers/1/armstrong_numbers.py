def is_armstrong_number(number):
    num = list(str(number))
    result = 0
    for i in num:
        result += int(i) ** len(num)
    if number == result:
        return True
    else:
        return False