import os

file_path = os.path.join('day_3', 'input')


def get_matching_number_at_position(position_index: int, index_ref_to_number: dict, numbers: list) -> int:
    if position_index in index_ref_to_number:
        number_index = index_ref_to_number[position_index]
        if not numbers[number_index][1]:
            numbers[number_index][1] = True
            return numbers[number_index][0]
    return 0


def sum_matching_numbers(symbol_metadata: list, index_ref_to_number: dict, numbers: list) -> int:
    total_sum = 0
    for index_symbol in symbol_metadata:
        total_sum += get_matching_number_at_position(index_symbol - 1, index_ref_to_number, numbers)
        total_sum += get_matching_number_at_position(index_symbol + 1, index_ref_to_number, numbers)
        total_sum += get_matching_number_at_position(index_symbol, index_ref_to_number, numbers)
    return total_sum


def save_line_data(line: str, index_ref_to_number: dict,
                   line_numbers: list, symbol_indexes: list) -> None:
    index_number = 0
    constructing_number = False
    for index, char in enumerate(line):
        if char.isdigit():
            if not constructing_number:
                constructing_number = True
                line_numbers.append([int(char), False])
            else:
                line_numbers[index_number][0] *= 10
                line_numbers[index_number][0] += int(char)
            index_ref_to_number[index] = index_number
            continue

        if constructing_number:
            constructing_number = False
            index_number += 1
        if char != '.':
            symbol_indexes.append(index)


def exo_1():
    total_sum = 0
    with open(file_path, 'r') as file:
        last_data = {'IRTN': {}, 'NBS': [], 'SI': []}

        for line in file:
            line = line[:len(line) - 1]
            index_ref_to_number = {}
            line_numbers = []
            symbol_indexes = []

            save_line_data(line, index_ref_to_number, line_numbers, symbol_indexes)

            all_symbol_indexes = symbol_indexes + last_data['SI']
            total_sum += sum_matching_numbers(all_symbol_indexes, index_ref_to_number, line_numbers)
            total_sum += sum_matching_numbers(symbol_indexes, last_data['IRTN'], last_data['NBS'])

            last_data = {
                'IRTN': index_ref_to_number,
                'NBS': line_numbers,
                'SI': symbol_indexes
            }

    return total_sum


def match_star_with_number(position_index: int, line_id: int,
                           symbol_data: list, index_ref_to_number: dict, numbers: list) -> bool:
    if position_index in index_ref_to_number:
        number_data = numbers[index_ref_to_number[position_index]]
        if len(number_data) == 1 or number_data[1] != line_id or number_data[2] != symbol_data[0]:
            number_data.append(line_id)
            number_data.append(symbol_data[0])
            symbol_data.append(number_data[0])
        return True
    return False


def find_numbers_matching_stars(symbol_metadata: dict, line_id: int,
                                index_ref_to_number: dict, numbers: list) -> None:
    for symbol_data in symbol_metadata[line_id]:
        match_star_with_number(symbol_data[0] - 1, line_id, symbol_data, index_ref_to_number, numbers)
        match_star_with_number(symbol_data[0], line_id, symbol_data, index_ref_to_number, numbers)
        match_star_with_number(symbol_data[0] + 1, line_id, symbol_data, index_ref_to_number, numbers)


def parse_line_numbers(line: str, index_ref_to_number: dict,
                      line_numbers: list, symbol_indexes: list) -> None:
    index_number = 0
    constructing_number = False
    for index, char in enumerate(line):
        if char.isdigit():
            if not constructing_number:
                constructing_number = True
                line_numbers.append([int(char)])
            else:
                line_numbers[index_number][0] *= 10
                line_numbers[index_number][0] += int(char)
            index_ref_to_number[index] = index_number
            continue

        if constructing_number:
            constructing_number = False
            index_number += 1
        if char == '*':
            symbol_indexes.append([index])


def compute_gear_ratio(symbol_indexes: dict) -> int:
    total_sum = 0
    for key in symbol_indexes:
        for star_data in symbol_indexes[key]:
            if len(star_data) == 3:
                total_sum += star_data[1] * star_data[2]
    return total_sum


def exo_2():
    with open(file_path, 'r') as file:
        symbol_indexes = {-1: []}
        last_data = {'IRTN': {}, 'NBS': []}

        for line_id, line in enumerate(file):
            line = line[:len(line) - 1]

            symbol_indexes[line_id] = []
            index_ref_to_number = {}
            line_numbers = []

            parse_line_numbers(line, index_ref_to_number, line_numbers, symbol_indexes[line_id])

            find_numbers_matching_stars(symbol_indexes, line_id, index_ref_to_number, line_numbers)
            find_numbers_matching_stars(symbol_indexes, line_id - 1, index_ref_to_number, line_numbers)
            find_numbers_matching_stars(symbol_indexes, line_id, last_data['IRTN'], last_data['NBS'])

            last_data = {
                'IRTN': index_ref_to_number,
                'NBS': line_numbers
            }

    return compute_gear_ratio(symbol_indexes)


print(f"{exo_1() = }")
print(f"{exo_2() = }")
