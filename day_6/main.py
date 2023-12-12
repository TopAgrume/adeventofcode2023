import os
import re

file_path = os.path.join('day_6', 'input')


def compute_distance(waiting: int, full_time: int) -> int:
    return waiting * (full_time - waiting)


def binary_search(time: int, target: int) -> int:
    low, high = 0, (time + 1) // 2

    while low <= high:
        mid = (low + high) // 2
        dist_val = compute_distance(mid, time)

        if dist_val == target:
            return time - (mid + 1) * 2
        elif dist_val < target:
            low = mid + 1
        else:
            high = mid - 1

    return time - (low + high)


def exo_1():
    with open(file_path, 'r') as file:
        times, distances = (re.findall(r'\d+', line) for line in file)
        times = map(int, times)
        distances = map(int, distances)

        total = 1
        for time, distance in zip(times, distances):
            total *= binary_search(time, distance)

        return total


def exo_2():
    with open(file_path, 'r') as file:
        times, distances = (re.findall(r'\d+', line) for line in file)
        time = int(''.join(times))
        distance = int(''.join(distances))

        return binary_search(time, distance)


print(f"{exo_1() = }")
print(f"{exo_2() = }")
