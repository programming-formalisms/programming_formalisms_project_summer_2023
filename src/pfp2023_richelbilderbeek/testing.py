"""General-purpose functions of moderate complexity.

Moderate complexity' means:
 * a cyclomatic complexity of 1 to 8
 * may have for-loops
 * maximally two variables modified
"""

from random import randint


def flip_coin():
    """Produce a random boolean."""
    return randint(0, 1) > 0 # noqa: S311

def get_digits(x):
    """Get the digits of an integer number.

    Get the digits of an integer number,
    for example, '123' becomes '[1, 2, 3]'
    and '0' becomes '[0]'.
    Negative numbers have only their digits collected,
    for example, '-123' becomes '[1, 2, 3]'.

    Will raise TypeError if `x` is not an integer.
    """
    if not isinstance(x, int):
        message = "'x' must be an integer"
        raise TypeError(message)
    zero = 0
    if x < zero:
        return get_digits(-x)
    digits = []
    digits_in_numbering_system = 10
    while True:
        digits.insert(0, x % digits_in_numbering_system)
        if x < digits_in_numbering_system:
            return digits
        x = x // digits_in_numbering_system

def roll_dice():
    """Produce a random integer, similar to a dice toll."""
    return randint(1, 6) # noqa: S311


def sum_primes(num):
    """Calculate the sum of all primes up to the given number."""
    if not isinstance(num, int):
        message = "'num' must be an integer"
        raise TypeError(message)
    primes = []
    two = 2
    if num > two:
        primes.append(two)
    elif num == two:
        return(two)
    else:
        return(0)
    for i in range(3, num+1, 2):
        not_prime = False
        for j in range(1, i):
            if i%j == 0 and j != 1:
                not_prime = True
                break
        if not not_prime:
            primes.append(i)
    return sum(primes)
