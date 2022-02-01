
"""
This function calculates the factorial function of the input number 
"""


def factorielle(n: int) -> int:
    if n == 0:
        return 1
    else:
        return n * factorielle(n-1)


print(factorielle(5))
