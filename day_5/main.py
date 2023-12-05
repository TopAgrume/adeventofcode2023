import os
import re

file_path = os.path.join('day_5', 'input')


def map_path(seeds: list, all_maps: dict) -> list:
    result = []
    for seed in seeds:
        tmp_node_value = seed
        for maps in all_maps.values():
            for start_source, end_source, dest in maps:
                if tmp_node_value < start_source or end_source < tmp_node_value:
                    continue

                tmp_node_value = dest + tmp_node_value - start_source
                break
        result.append(tmp_node_value)
    return result


def parse_input() -> tuple[list, dict]:
    all_maps = {}

    with open(file_path, 'r') as file:
        f_line = file.readline().strip()
        numbers = re.findall(r'\d+', f_line)
        seeds = [int(num) for num in numbers]

        map_count = -1
        file.readline()

        for line in file:
            line = line.strip()
            if not line:
                continue

            if line[0].isalpha():
                map_count += 1
                all_maps[map_count] = []
                continue

            numbers = re.findall(r'\d+', line)
            range_val = int(numbers[2])
            if range_val == 0:
                continue

            dest, source = int(numbers[0]), int(numbers[1])

            line_data = [source, source + range_val - 1, dest]
            all_maps[map_count].append(line_data)

    return seeds, all_maps


def exo_1():
    seeds, all_maps = parse_input()
    locations = map_path(seeds, all_maps)
    return min(locations)


def exo_2():
    seeds, all_maps = parse_input()
    ranges = [[start, end + start] for start, end in zip(seeds[::2], seeds[1::2])]

    for maps in all_maps.values():
        results = []

        while len(ranges) != 0:
            start_range, end_range = ranges.pop()

            for start_source, end_source, dest in maps:
                offset = dest - start_source

                # Avoid non matching maps
                if end_range <= start_source or end_source <= start_range:
                    continue

                # Save unmatch range inside list (inf part)
                if start_range < start_source:
                    ranges.append([start_range, start_source])
                    start_range = start_source

                # Save unmatch range inside list (supp part)
                if end_source < end_range:
                    ranges.append([end_source, end_range])
                    end_range = end_source

                # The rest of the interval
                results.append([start_range + offset, end_range + offset])
                break
            else:
                # Save non matching for next mapping
                results.append([start_range, end_range])

        ranges = results

    return min(loc[0] for loc in ranges)


print(f"{exo_1() = }")
print(f"{exo_2() = }")
