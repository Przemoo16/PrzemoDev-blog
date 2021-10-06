import sys
from timeit import default_timer as timer
from typing import Any, Callable, Dict, Union
import uuid

from recursion_and_iteration import JSON_TYPE, flatten_iteration, flatten_recursion


def create_nested_dict(num_branches: int, depth: int) -> Dict[str, Any]:
    output_dict: Dict[str, Any] = {}
    level = output_dict
    for _ in range(num_branches):
        for _ in range(depth):
            key = str(uuid.uuid4())
            level = level.setdefault(key, {})
        level = output_dict
    return output_dict


def get_execution_time(
    func: Callable[..., JSON_TYPE], *args: Union[JSON_TYPE, str]
) -> float:
    start = timer()
    func(*args)
    end = timer()
    return end - start


def main() -> None:
    print("Recursion limit:", sys.getrecursionlimit())
    new_recursion_limit = 5000  # Warning: Too big value here may lead to errors
    sys.setrecursionlimit(new_recursion_limit)
    print("Changed recursion limit to:", sys.getrecursionlimit())

    nested_dict = create_nested_dict(num_branches=100, depth=4000)

    print("Recursion time:", get_execution_time(flatten_recursion, nested_dict))
    print("Iteration time:", get_execution_time(flatten_iteration, nested_dict))


if __name__ == "__main__":
    main()
