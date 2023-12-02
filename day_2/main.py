import os

file_path = os.path.join('day_2', 'input')


def check_sets_in_game(game_id: int, games: str, max_balls: dict) -> int:
    for ball_set in games.split(';'):
        for color_conf in ball_set.split(','):
            words = color_conf.split()
            number = int(words[0])
            color = words[1]
            if max_balls[color] < number:
                return 0
    return game_id


def exo_1() -> int:
    max_balls = {'red': 12, 'green': 13, 'blue': 14}
    sum_game_id = 0
    with open(file_path, 'r') as file:
        for game_id, line in enumerate(file, 1):
            games = line.split(':')[1]
            sum_game_id += check_sets_in_game(game_id, games, max_balls)

    return sum_game_id


print(f"{exo_1() = }")
