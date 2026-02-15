from src.main import factorial


def test_factorial_simple() -> None:
    assert factorial(5) == 120
    assert factorial(6) == 720
    assert factorial(10) == 3628800