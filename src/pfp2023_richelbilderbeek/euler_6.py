def sum_square_differences(n):
    """Calculates the difference between the sum of squares of numbers and the
    square of the sum of numbers

    Parameters
    ----------
    n: int
        Highest number to consider

    Returns
    -------
    : int
        Returns the difference"""
    if not isinstance(n, int):
        raise TypeError(f"n <{n}> needs to be an integer")
    pass