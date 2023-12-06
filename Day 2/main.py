rgb_max = [12,13,14]

def convert_set_to_rgb(set):
    new_set = [0, 0, 0]
    for i in range(len(set)):
        if " red" in set[i]:
            red = int(set[i].replace(" red", ""))
            new_set[0] = red
        elif " green" in set[i]:
            green = int(set[i].replace(" green", ""))
            new_set[1] = green
        elif " blue" in set[i]:
            blue = int(set[i].replace(" blue", ""))
            new_set[2] = blue
    return new_set


def parse_input(file_name):
    with open(file_name, 'r') as file:
        input = file.read().splitlines()
    parsed_input = []
    for line in input:
        line_without_game = line[line.find(':') + 2:]
        line_split_games = line_without_game.split('; ')
        line_split_sets = []
        for set in line_split_games:
            line_split_sets.append(set.split(', '))
        parsed_input.append(line_split_sets)
    return parsed_input


def find_possible_games_sum(input):
    possible_game_idxs = []
    for game_idx in range(len(input)):
        possible = 1
        for set_idx in range(len(input[game_idx])):
            if input[game_idx][set_idx][0] > rgb_max[0] or input[game_idx][set_idx][1] > rgb_max[1] or \
                    input[game_idx][set_idx][2] > rgb_max[2]:
                possible = 0
        if possible:
            possible_game_idxs.append(game_idx + 1)

    return sum(possible_game_idxs)

def minimum_power(input):
    power = 0
    for game_idx in range(len(input)):
        min_rgb = [0,0,0]
        for set_idx in range(len(input[game_idx])):
            if input[game_idx][set_idx][0] > min_rgb[0]:
                min_rgb[0] = input[game_idx][set_idx][0]
            if input[game_idx][set_idx][1] > min_rgb[1]:
                min_rgb[1] = input[game_idx][set_idx][1]
            if input[game_idx][set_idx][2] > min_rgb[2]:
                min_rgb[2] = input[game_idx][set_idx][2]
        power += min_rgb[0]*min_rgb[1]*min_rgb[2]
    return power


if __name__ == '__main__':
    input = parse_input("input.txt")
    for game_idx in range(len(input)):
        for set_idx in range(len(input[game_idx])):
            input[game_idx][set_idx] = convert_set_to_rgb(input[game_idx][set_idx])
    print(f"Part 1: {find_possible_games_sum(input)}")
    print(f"Part 2: {minimum_power(input)}")