"""
Function that calcultes recursively the fibonacci number
"""

import numpy as np
import errors

maxNumber = 1e20
minNumber = 1e-20


def fibonacci_of(n):
    if n in {0, 1}:  # Base case
        return n
    return fibonacci_of(n - 1) + fibonacci_of(n - 2)


def verifyNumber(input):
    if type(input) != int and np.iscomplex(input) != False:
        raise ValueError("haha")
    elif input < 0:
        raise errors.NegativeValue
    elif input > maxNumber:
        raise errors.ValueTooLargeError
    elif input < minNumber:
        raise errors.ValueTooSmallError
    elif type(input) == str:
        raise errors.ValueStrError
    elif np.iscomplex(input):
        raise errors.ValueComplexError

    else:
        return input


def input_fibo() -> int:
    while True:
        try:
            n = input("Entrer un nombre: ")
            if n.isnumeric():
                n = int(n)
                verifyNumber(n)
                break
            try:
                try:
                    n = complex(n)
                    if np.iscomplex(n):
                        print("The value is complex please try again")
                except errors.ValueComplexError:
                    print("the input value is complex")
                n = str(n)
                if type(n) == str:
                    print("enter a number")
                verifyNumber(n)
            except errors.ValueStrError:
                print("Retry")
        except errors.NegativeValue:
            print("Please enter a positive number")
            continue

        except errors.ValueTooLargeError:
            print("Please enter a smaller number")
            continue
        except errors.ValueTooSmallError:
            print("Please enter a bigger number")
            continue
        except ValueError:
            break
    return n


res = [fibonacci_of(n) for n in range(input_fibo())]
print("La suite de fibonacci est:")
print(*res, sep=", ")
