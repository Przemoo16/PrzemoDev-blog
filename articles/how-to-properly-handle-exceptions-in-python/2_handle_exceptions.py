from typing import List


class User:
    def __init__(self, name: str, last_name: str):
        self.name = name
        self.last_name = last_name


def ignoring_exception() -> None:
    users: List[User] = []
    user = User(name="John", last_name="Green")
    try:
        raise ConnectionError("Database connection error")
        users.append(user)  # pylint: disable=unreachable
    except ConnectionError:
        pass
    else:
        print("User has been added to the database successfully")


def logging_exception() -> None:
    users: List[User] = []
    user = User(name="John", last_name="Green")
    try:
        raise ConnectionError("Database connection error")
        users.append(user)  # pylint: disable=unreachable
    except ConnectionError:
        print("Connection error. User has not been added to the database")
    else:
        print("User has been added to the database successfully")


def main() -> None:
    ignoring_exception()
    logging_exception()


if __name__ == "__main__":
    main()
