from datetime import datetime

from dateutil import parser
from dateutil.relativedelta import relativedelta


def convert_to_datetime(date: str) -> datetime:
    return parser.parse(date, ignoretz=True)


def count_years_delta(start_date: datetime, end_date: datetime) -> int:
    return relativedelta(end_date, start_date).years


def too_many_tasks() -> None:
    user_data = {"name": "John", "date_of_birth": "invalid_date"}
    try:
        date_of_birth_str = user_data["date_of_birth"]
        date_of_birth = convert_to_datetime(date_of_birth_str)
        now = datetime.utcnow()
        age = count_years_delta(date_of_birth, now)
        print(f"The user have {age} years old")
    except ValueError:
        print("Invalid user's date of birth")


def minimum_tasks() -> None:
    user_data = {"name": "John", "date_of_birth": "invalid_date"}
    date_of_birth_str = user_data["date_of_birth"]
    try:
        date_of_birth = convert_to_datetime(date_of_birth_str)
    except ValueError:
        print("Invalid user's date of birth")
    else:
        now = datetime.utcnow()
        age = count_years_delta(date_of_birth, now)
        print(f"The user have {age} years old")


def main() -> None:
    too_many_tasks()
    minimum_tasks()


if __name__ == "__main__":
    main()
