from typing import TypedDict


class Item(TypedDict):
    id: str
    name: str
    price: float
    quantity: int
    colors: list[str]


class ItemWithDiscount(Item):
    discount: float


def count_price_with_discount(item: ItemWithDiscount) -> float:
    return item["price"] * item["quantity"] * (1 - item["discount"])


def main() -> None:
    shoes: ItemWithDiscount = {
        "id": "2",
        "name": "Shoes",
        "price": 155.0,
        "quantity": 1,
        "colors": ["black"],
        "discount": 0.1,
    }
    print(f"Price with discount: {count_price_with_discount(shoes)}")


if __name__ == "__main__":
    main()
