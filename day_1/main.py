import os

file_path = os.path.join('day_1', 'input')


def exo_1() -> int:
    total_sum = 0
    with open(file_path, 'r') as file:
        for line in file:
            for char in line:
                if char.isdigit():
                    total_sum += int(char) * 10
                    break
            for char in line[::-1]:
                if char.isdigit():
                    total_sum += int(char)
                    break
    return total_sum


def get_first_char(line: str, digit_mapping: dict) -> int:
    base_index, total_sum = 0, 0

    while base_index < len(line) - 2:
        key = ""
        for explor_index, char in enumerate(line[base_index:min(base_index + 5, len(line))]):
            if len(key) <= 3 and char.isdigit():
                return int(char) * 10
            key += char
            if len(key) > 2 and key in digit_mapping:
                return digit_mapping[key] * 10
        base_index += 1
    return total_sum


def get_last_char(line: str, digit_mapping: dict) -> int:
    base_index, total_sum = len(line), 0

    while base_index > 0:
        key = ""
        for explor_index in range(max(0, base_index - 6), base_index - 1)[::-1]:
            char = line[explor_index]
            if len(key) <= 3 and char.isdigit():
                return int(char)
            key = char + key
            if len(key) > 2 and key in digit_mapping:
                return digit_mapping[key]
        base_index -= 1
    return total_sum


def exo_2() -> int:
    digit_mapping = {
        'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
        'six': 6, 'seven': 7, 'eight': 8, 'nine': 9
    }
    total_sum = 0
    with open(file_path, 'r') as file:
        for line in file:
            total_sum += get_first_char(line, digit_mapping)
            total_sum += get_last_char(line, digit_mapping)

    return total_sum


print(f"{exo_1() = }")
print(f"{exo_2() = }")
