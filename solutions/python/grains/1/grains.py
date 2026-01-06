def square(number):
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    return 1 << (number - 1)  # или: 2 ** (number - 1)

def total():
    # Сумма геометрической прогрессии: 2^0 + 2^1 + ... + 2^63 = 2^64 - 1
    return (1 << 64) - 1  # или: (2**64) - 1