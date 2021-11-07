from typing import Any


def low_level_exceptions() -> None:
    def validate_request(payload: Any) -> None:
        if not isinstance(payload, dict):
            raise ValueError("Request payload must be a type of dict")
        if not payload.get("salary"):
            raise KeyError("'salary' must be a part of request payload")
        if not isinstance(payload["salary"], int):
            raise ValueError("'salary' must be a type of int")

    request = {"salary": "invalid_salary"}
    try:
        validate_request(request)
    except (KeyError, ValueError) as e:
        print(e)


def custom_exceptions() -> None:
    class ValidationError(Exception):
        pass

    def validate_request(payload: Any) -> None:
        if not isinstance(payload, dict):
            raise ValidationError("Request payload must be a type of dict")
        if not payload.get("salary"):
            raise ValidationError("'salary' must be a part of request payload")
        if not isinstance(payload["salary"], int):
            raise ValidationError("'salary' must be a type of int")

    request = {"salary": "invalid_salary"}
    try:
        validate_request(request)
    except ValidationError as e:
        print(e)


def main() -> None:
    low_level_exceptions()
    custom_exceptions()


main()
