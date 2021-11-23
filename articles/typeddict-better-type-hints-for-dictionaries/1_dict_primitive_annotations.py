from typing import Any, cast


def count_price_dict(item: dict) -> float:  # type: ignore
    # print("Price: " + item["price"])  # TypeError
    return item["price"] * item["quantity"]


def count_price_any(item: dict[str, Any]) -> float:
    return item["price"] * item["quantity"]


def count_price_union(item: dict[str, str | float | int | list[str]]) -> float:
    return item["price"] * item["quantity"]  # type: ignore


def count_price_union_cast(item: dict[str, str | float | int | list[str]]) -> float:
    price = cast(float, item["price"])
    quantity = cast(int, item["quantity"])
    return price * quantity


def main() -> None:
    ball = {
        "id": "1",
        "name": "Ball",
        "price": 20.0,
        "quantity": 2,
        "colors": ["red", "blue"],
    }
    print(f"Price: {count_price_dict(ball)}")
    print(f"Price: {count_price_any(ball)}")
    print(f"Price: {count_price_union(ball)}")  # type: ignore
    print(f"Price: {count_price_union_cast(ball)}")  # type: ignore


if __name__ == "__main__":
    main()
