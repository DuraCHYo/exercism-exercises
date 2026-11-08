def equilateral(sides):
    return False if 0 in sides else max(sides) == min(sides)

def isosceles(sides):
    a, b, c = sorted(sides)
    return (a + b > c) and (a == b or b == c)

from collections import Counter
def scalene(sides):
    a, b, c = sorted(sides)
    return False if 0 in sides else ((a + b > c) and not any(value != 1 for value in Counter(sides).values()))
