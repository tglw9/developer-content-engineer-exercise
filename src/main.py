import time
import sys
import math

def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("factorial() not defined for negative values")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


if __name__ == "__main__":
    result = factorial(5)
    print(f"Factorial of 5 is {result}")