class InvalidArguments(Exception):
    pass


def sum_two_numbers(a: float, b: float) -> float:
    return a + b


def not_re_raising_exceptions() -> None:
    try:
        print(sum_two_numbers(None, "text"))  # type: ignore
    except TypeError:
        raise InvalidArguments(  # pylint: disable=raise-missing-from
            "Invalid arguments passed to the function"
        )


def explicitly_re_raising_exceptions() -> None:
    try:
        print(sum_two_numbers(None, "text"))  # type: ignore
    except TypeError as e:
        raise InvalidArguments("Invalid arguments passed to the function") from e


def main() -> None:
    # not_re_raising_exceptions()
    explicitly_re_raising_exceptions()


main()
