from src.main import factorial


def test_factorial_zero() -> None:
    assert factorial(0) == 1


def test_factorial_one() -> None:
    assert factorial(1) == 1


def test_factorial_positive() -> None:
    assert factorial(5) == 120
    assert factorial(6) == 720
    assert factorial(10) == 3628800


# def test_factorial_negative_raises() -> None:
#     with pytest.raises(ValueError, match="not defined for negative"):
#         factorial(-1)
#     with pytest.raises(ValueError, match="not defined for negative"):
#         factorial(-10)