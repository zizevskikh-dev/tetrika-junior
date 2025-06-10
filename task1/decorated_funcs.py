from task1.strict_types_decorator import strict


@strict
def sum_two(a: int, b: int):
    """
    Adds two objects together.

    Args:
        a : The first operand.
        b : The second operand.

    Returns:
        The sum or concatenation of the two operands.
    """
    return a + b
