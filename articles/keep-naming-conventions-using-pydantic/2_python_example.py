from typing import List


def sum_even_numbers(numbers: List[int]) -> int:
    even_numbers = [number for number in numbers if number % 2 == 0]
    return sum(even_numbers)


if __name__ == "__main__":
    example_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(sum_even_numbers(example_numbers))
