def leap_year(year):
    # если делится на 4 без остатка или делится на 400 без остатка и если делится на 100 с остатком
    if ((year % 4 == 0 or year % 400 == 0) and (year % 100 != 0)) or year % 400 == 0:
        return True
    else:
        return False
