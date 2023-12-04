import os
import re

file_path = os.path.join('day_4', 'input')


def exo_1():
    total_sum = 0
    with open(file_path, 'r') as file:
        for line in file:
            pow_number = 1
            numbers = line.split(':')[1].split('|')
            winning_part, classic_part = numbers[0], numbers[1]

            numbers = re.findall(r'\d+', classic_part)
            classic_numbers = [int(num) for num in numbers]

            pattern = re.compile(r'\d+')
            matches = pattern.finditer(winning_part)

            for match in matches:
                winning_number = match.group()
                if int(winning_number) in classic_numbers:
                    pow_number *= 2

            total_sum += (pow_number // 2) if pow_number != 0 else None
    return total_sum


def count_matches(matches, classic_numbers: list, next_copy_nb_queue: list) -> int:
    match_count = 0
    for match in matches:
        winning_number = match.group()
        if not int(winning_number) in classic_numbers:
            continue
        if len(next_copy_nb_queue) == match_count:
            next_copy_nb_queue.append(1)
        match_count += 1
    return match_count


def exo_2():
    total_sum = 0
    with open(file_path, 'r') as file:
        next_copy_nb_queue = []

        for line in file:
            game = line.split(':')[1]
            numbers = game.split('|')
            winning_part = numbers[0]
            classic_part = numbers[1]

            numbers = re.findall(r'\d+', classic_part)
            classic_numbers = [int(num) for num in numbers]

            current_copy_nb = 1
            if len(next_copy_nb_queue) != 0:
                current_copy_nb = next_copy_nb_queue.pop(0)

            pattern = re.compile(r'\d+')
            matches = pattern.finditer(winning_part)
            match_count = count_matches(matches, classic_numbers, next_copy_nb_queue)

            for index in range(match_count):
                next_copy_nb_queue[index] += current_copy_nb

            total_sum += current_copy_nb
    return total_sum


print(f"{exo_1()}")
print(f"{exo_2()}")
