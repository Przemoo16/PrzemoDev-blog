import collections
from typing import Any, Deque, Dict, List, Tuple, Union

JSON_VALUE = Union[str, int, float, bool, None, List[Any], Dict[str, Any]]
JSON_TYPE = Dict[str, JSON_VALUE]
QUEUE = Deque[Tuple[str, JSON_VALUE]]


def flatten_recursion(input_dict: JSON_TYPE, parent_key: str = "") -> JSON_TYPE:
    output_dict: JSON_TYPE = {}
    for key, value in input_dict.items():
        new_key = f"{parent_key}.{key}" if parent_key else key
        if isinstance(value, dict):
            output_dict.update(flatten_recursion(value, new_key))
        else:
            output_dict[new_key] = value
    return output_dict


def flatten_iteration(input_dict: JSON_TYPE) -> JSON_TYPE:
    queue: QUEUE = collections.deque([("", input_dict)])
    output_dict: JSON_TYPE = {}
    while queue:
        key, value = queue.popleft()
        if isinstance(value, dict):
            prefix = f"{key}." if key else ""
            queue.extend((f"{prefix}{k}", v) for k, v in value.items())
        else:
            output_dict[key] = value
    return output_dict


def main() -> None:
    job_profile: JSON_TYPE = {
        "name": "Tom",
        "last_name": "Novak",
        "age": 30,
        "job": {
            "position": "Python Developer",
            "working_time_years": 3,
            "company": {
                "name": "Great Software House",
                "address": {
                    "city": {
                        "name": "London",
                        "number_of_people_mln": 8.982,
                    },
                    "street": "Example Street",
                    "street_number": "501a",
                    "flat_number": None,
                    "postal_code": " DA15 7XZ",
                },
            },
        },
    }

    flattened_recursion = flatten_recursion(job_profile)
    flattened_iteration = flatten_iteration(job_profile)

    print("Recursion:", flattened_recursion)
    print("Iteration:", flattened_iteration)
    print("Are equal?:", flattened_recursion == flattened_iteration)


if __name__ == "__main__":
    main()
