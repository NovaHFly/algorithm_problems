from typing import TextIO


def get_input(io: TextIO) -> tuple[list[int], int]:
    """Get input data from text io."""
    weights = [int(weight) for weight in io.readline().split()]
    weight_limit = int(io.readline())
    return weights, weight_limit


def calculate_platform_amount(
    robot_weights: list[int], weight_limit: int
) -> int:
    """Calculate the amount of platforms needed to transport robots.

    Args:
        robot_weights (list[int]): Array of robot weights.
        weight_limit (int): Maximum weight limit of a platform.

    Returns:
        int: Amount of transport platforms.
    """
    # Sort the array for two pointers to work
    robot_weights = sorted(robot_weights)
    print(robot_weights)

    count_platforms = 0

    # Left-most and right-most array indexes
    left_id = 0
    right_id = len(robot_weights) - 1

    # Loop while we still have elements
    while left_id <= right_id:
        # Each iteration we load one platform
        count_platforms += 1

        # If only one robot remains, exit loop
        if left_id == right_id:
            break

        sum_weights = robot_weights[left_id] + robot_weights[right_id]

        # If sum of pair of elements exceeds the limit
        #  only the biggest one will be loaded
        if sum_weights > weight_limit:
            right_id -= 1
            continue

        # Exclude 2 loaded elements
        left_id += 1
        right_id -= 1

    return count_platforms


if __name__ == '__main__':
    with open('delivery_input.txt', encoding='UTF-8') as f:
        robot_weights, weight_limit = get_input(f)

    print(calculate_platform_amount(robot_weights, weight_limit))
