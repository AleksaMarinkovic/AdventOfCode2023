import re


def is_char_digit(char):
    return 48 <= int(ord(char)) <= 57


def parse_input(file_name):
    with open(file_name, 'r') as file:
        input = file.read().splitlines()
    for line_idx in range(len(input)):
        input[line_idx] = re.sub(r'\bCard\s+\d+:', '', input[line_idx])
        number_of_spaces = 0
        char_idx = 0
        while not is_char_digit(input[line_idx][char_idx]):
            char_idx += 1
        input[line_idx] = input[line_idx][char_idx:]
        input[line_idx] = input[line_idx].split(' | ')
        char_idx = 0
        while not is_char_digit(input[line_idx][1][char_idx]):
            char_idx += 1
        input[line_idx][1] = input[line_idx][1][char_idx:]
        input[line_idx][0] = input[line_idx][0].replace("  ", " ")
        input[line_idx][0] = input[line_idx][0].split(" ")
        input[line_idx][1] = input[line_idx][1].replace("  ", " ")
        input[line_idx][1] = input[line_idx][1].split(" ")
        for number_idx in range(len(input[line_idx][0])):
            input[line_idx][0][number_idx] = int(input[line_idx][0][number_idx])
        for number_idx in range(len(input[line_idx][1])):
            input[line_idx][1][number_idx] = int(input[line_idx][1][number_idx])
    return input


def get_score_from_card(card):
    score = 0
    for number_idx in range(len(card[1])):
        if card[1][number_idx] in card[0]:
            if score == 0:
                score += 1
            else:
                score *= 2
    return score


def get_matches_from_card(card):
    matches = 0
    for number_idx in range(len(card[1])):
        if card[1][number_idx] in card[0]:
            matches += 1
    return matches


if __name__ == '__main__':
    input = parse_input("input.txt")
    total_score = 0
    for card_idx in range(len(input)):
        total_score += get_score_from_card(input[card_idx])
    # for part 2 we append the total amount of copies, starting from 1
    for card_idx in range(len(input)):
        input[card_idx].append(1)
    for card_idx in range(len(input)):
        matches = get_matches_from_card(input[card_idx])
        for amount in range(1, matches + 1, 1):
            input[card_idx + amount][2] += 1 * input[card_idx][2]
    total_number_of_copies = 0
    for card_idx in range(len(input)):
        total_number_of_copies += input[card_idx][2]
    # part 1 solution
    print(total_score)
    # part 2 solution
    print(total_number_of_copies)
