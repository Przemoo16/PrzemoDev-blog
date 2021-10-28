# pylint: disable=undefined-variable


def bare_except() -> None:
    while True:
        try:
            first_number = int(input("First number: "))
            second_number = int(input("Second number: "))
        except:  # pylint: disable=bare-except # noqa: E722
            print("Invalid input number")
        else:
            print(f"Sum: {first_number+second_number}")


def exception_class() -> None:
    try:
        first_number = int(input("First number: "))
        second_number = intt(input("Second number: "))  # type: ignore # noqa: F821
    except Exception:  # pylint: disable=broad-except
        print("Invalid input number")
    else:
        print(f"Sum: {first_number+second_number}")


def specific_exception() -> None:
    try:
        first_number = int(input("First number: "))
        second_number = int(input("Second number: "))
    except ValueError:
        print("Invalid input number")
    else:
        print(f"Sum: {first_number+second_number}")


def main() -> None:
    # bare_except()  # Executes the loop which cannot be stopped using Ctrl-C
    exception_class()
    specific_exception()


if __name__ == "__main__":
    main()
