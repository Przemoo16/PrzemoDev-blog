def repeated_exceptions() -> None:
    user_data = {"name": "John", "age": "invalid_age"}
    try:
        age = int(user_data["age"])
    except KeyError:
        print("Invalid age data")
    except TypeError:
        print("Invalid age data")
    except ValueError:
        print("Invalid age data")
    else:
        print(f"Next year, the user will be {age + 1} years old")


def merged_exceptions() -> None:
    user_data = {"name": "John", "age": "invalid_age"}
    try:
        age = int(user_data["age"])
    except (KeyError, TypeError, ValueError):
        print("Invalid age data")
    else:
        print(f"Next year, the user will be {age + 1} years old")


def main() -> None:
    repeated_exceptions()
    merged_exceptions()


if __name__ == "__main__":
    main()
