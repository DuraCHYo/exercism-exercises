def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    result = sum(item for item in range(1, number) if number % item == 0)
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    if result > number:
        return "abundant"
    if result < number:
        return "deficient"
    return "perfect"
