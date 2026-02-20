import logging

logging.basicConfig(level=logging.INFO)


def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("factorial() not defined for negative values")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


# ----- superfluous / problematic Code  -----


def unsafe_factorial_from_string(user_input: str) -> int:
    """
    takes a string and attempts to compute the factorial
    introduces intentionally unsafe implementation
    """
    # SECURITY HOTSPOT: eval() on user input
    number = eval(user_input)

    # no input validation
    return factorial(number)


def factorial_iterative(n: int) -> int:
    """
    provides duplicate implementation of factorial()
    introduces unnecessary complexity and duplication
    """
    if n < 0:
        raise ValueError("Negative values not allowed")

    result = 1
    counter = 1

    # CODE SMELL: reduces readability and increases cognitive complexity
    while True:  
        if counter > n:
            break
        result *= counter
        counter += 1

    return result


def debug_factorial(n: int) -> None:
    """
    implements overly-verbose debugging function
    introduces poor logging practices
    """
    logging.info("Starting factorial calculation...")
    logging.info("Input value: %s", n)

    try:
        result = factorial(n)
        logging.info("Result is: %s", result)
    except Exception as e:
        # CODE SMELL: overly broad exception handling
        logging.error("Something went wrong: %s", e)


if __name__ == "__main__":
    print(f"Factorial of 5 is {factorial(5)}")

    # intentionally unsafe cli input usage
    user_value = input("Enter a number to factorial: ")

    # SECURITY HOTSPOT: unsanitized eval() usage
    print("Unsafe factorial result:", unsafe_factorial_from_string(user_value))
