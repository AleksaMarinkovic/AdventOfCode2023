import math


def is_char_digit(char):
    return 48 <= int(ord(char)) <= 57


def parse_input1(file_name):
    with open(file_name, 'r') as file:
        input = file.read().splitlines()
    for line_idx in range(len(input)):
        for char_idx in range(len(input[line_idx])):
            if is_char_digit(input[line_idx][char_idx]):
                input[line_idx] = input[line_idx][char_idx:].split(" ")
                break
    for line_idx in range(len(input)):
        input[line_idx] = list(filter(lambda x: x != '', input[line_idx]))
    races = []
    for i in range(len(input[0])):
        races.append([input[0][i], input[1][i]])
    for race_idx in range(len(races)):
        for j in range(len(races[race_idx])):
            races[race_idx][j] = int(races[race_idx][j])
    return races


def parse_input2(file_name):
    with open(file_name, 'r') as file:
        input = file.read().splitlines()
    for line_idx in range(len(input)):
        for char_idx in range(len(input[line_idx])):
            if is_char_digit(input[line_idx][char_idx]):
                input[line_idx] = input[line_idx][char_idx:].split(" ")
                break
    for line_idx in range(len(input)):
        input[line_idx] = list(filter(lambda x: x != '', input[line_idx]))
    race_time = ""
    race_distance = ""
    for i in range(len(input[0])):
        race_time += input[0][i]
        race_distance += input[1][i]
    return [int(race_time),int(race_distance)]


def number_of_ways_to_win(time, distance):
    ways_to_win = 0
    x1 = (time + math.sqrt(time ** 2 - 4 * distance)) / 2
    x2 = (time - math.sqrt(time ** 2 - 4 * distance)) / 2
    new_x1 = math.ceil(min(x1, x2))
    new_x2 = math.floor(max(x1, x2))
    if min(x1, x2) == new_x1 and max(x1, x2) == new_x2:
        return new_x2-new_x1-1
    return new_x2-new_x1+1


if __name__ == '__main__':
    races = parse_input1("input.txt")
    number_of_ways_to_beat_records1 = 1
    for race in races:
        number_of_ways_to_beat_records1 *= number_of_ways_to_win(race[0], race[1])
    print(f"Part 1: {int(number_of_ways_to_beat_records1)}")

    race = parse_input2("input.txt")
    number_of_ways_to_beat_record2 = number_of_ways_to_win(race[0], race[1])
    print(f"Part 2: {int(number_of_ways_to_beat_record2)}")
