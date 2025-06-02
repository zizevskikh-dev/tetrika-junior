from task1.solution import sum_two


def main() -> None:
    """
    Entry point of annotation decorator realisation.

    cCalls the `sum_two` function with two objects and returns the result.
    """
    return sum_two(a=1, b=2)


if __name__ == "__main__":
    main()
