from typing import TypedDict


class Item(TypedDict, total=False):
    id: str
    name: str
    price: float
    quantity: int
    colors: list[str]


def main() -> None:
    gloves: Item = {
        "id": "4",
        "name": "Gloves",
        "price": 15.0,
        "quantity": 1,
    }
    print(f"Item without colors field: {gloves}")


if __name__ == "__main__":
    main()
