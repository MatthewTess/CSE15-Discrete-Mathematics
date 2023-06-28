
import random


def gen_random_list(n):
    """
    Generates a list with n non-negative random integers

    Parameters
    ----------
    n : int
        Number of elements in the list. Must be positive.

    Returns
    -------
    List with n non-negative random integers

    """

    assert n > 0
    l = [random.randint(0, 10 * n) for _ in range(n)]
    return l


if __name__ == '__main__':
    l = gen_random_list(10)
    print(l)
