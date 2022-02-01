

"""
This function returns the result of the polynome operation
"""


def Polynome(x: int) -> int:
    result = x**3 - 1.5 * x**2 - 6*x + 5
    return result


print(Polynome(5))
