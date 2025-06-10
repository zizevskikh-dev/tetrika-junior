from task1.decorated_funcs import sum_two


def main() -> None:
    """
    Entry point of annotation decorator realisation.

    Calls the `sum_two` function with two operands and prints the result.
    """
    print(sum_two(a=1, b=2))


if __name__ == "__main__":
    main()
