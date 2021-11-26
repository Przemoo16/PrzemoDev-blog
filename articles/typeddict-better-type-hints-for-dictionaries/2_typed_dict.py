from typing import TypedDict


class Item(TypedDict):
    id: str
    name: str
    price: float
    quantity: int
    colors: list[str]


def count_price(item: Item) -> float:
    return item["price"] * item["quantity"]


def main() -> None:
    ball: Item = {
        "id": "1",
        "name": "Ball",
        "price": 20.0,
        "quantity": 2,
        "colors": ["red", "blue"],
    }
    print(f"Price: {count_price(ball)}")


if __name__ == "__main__":
    main()
