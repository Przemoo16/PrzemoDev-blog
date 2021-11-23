from typing import TypedDict


class Item(TypedDict):
    id: str
    name: str
    price: float
    quantity: int
    colors: list[str]


class Cart(TypedDict):
    total_price: float
    items: list[Item]


def create_cart(items: list[Item]) -> Cart:
    total_price = sum(count_price(item) for item in items)
    return {
        "total_price": total_price,
        "items": items,
    }


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
    t_shirt: Item = {
        "id": "3",
        "name": "T-shirt",
        "price": 60.0,
        "quantity": 3,
        "colors": ["black", "white", "red"],
    }
    cart = create_cart([ball, t_shirt])
    print(f"Cart: {cart}")


if __name__ == "__main__":
    main()
