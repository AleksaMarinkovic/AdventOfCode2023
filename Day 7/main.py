from collections import Counter
import operator


def map_char_to_int(char, reverse=0):
    if not reverse:
        if char == '1':
            return 1
        elif char == '2':
            return 2
        elif char == '3':
            return 3
        elif char == '4':
            return 4
        elif char == '5':
            return 5
        elif char == '6':
            return 6
        elif char == '7':
            return 7
        elif char == '8':
            return 8
        elif char == '9':
            return 9
        elif char == 'T':
            return 10
        elif char == 'J':
            return 11
        elif char == 'Q':
            return 12
        elif char == 'K':
            return 13
        elif char == 'A':
            return 14
    else:
        if char == 1:
            return "1"
        elif char == 2:
            return "2"
        elif char == 3:
            return "3"
        elif char == 4:
            return "4"
        elif char == 5:
            return "5"
        elif char == 6:
            return "6"
        elif char == 7:
            return "7"
        elif char == 8:
            return "8"
        elif char == 9:
            return "9"
        elif char == 10:
            return "T"
        elif char == 11:
            return "J"
        elif char == 12:
            return "Q"
        elif char == 13:
            return "K"
        elif char == 14:
            return "A"

def map_char_to_int_joker(char, reverse=0):
    if not reverse:
        if char == 'J':
            return 1
        elif char == '2':
            return 2
        elif char == '3':
            return 3
        elif char == '4':
            return 4
        elif char == '5':
            return 5
        elif char == '6':
            return 6
        elif char == '7':
            return 7
        elif char == '8':
            return 8
        elif char == '9':
            return 9
        elif char == 'T':
            return 10
        elif char == 'Q':
            return 11
        elif char == 'K':
            return 12
        elif char == 'A':
            return 13
    else:
        if char == 1:
            return "J"
        elif char == 2:
            return "2"
        elif char == 3:
            return "3"
        elif char == 4:
            return "4"
        elif char == 5:
            return "5"
        elif char == 6:
            return "6"
        elif char == 7:
            return "7"
        elif char == 8:
            return "8"
        elif char == 9:
            return "9"
        elif char == 10:
            return "T"
        elif char == 11:
            return "Q"
        elif char == 12:
            return "K"
        elif char == 13:
            return "A"


def parse_input(file_name):
    with open(file_name, 'r') as file:
        input = file.read().splitlines()
    for line_idx in range(len(input)):
        input[line_idx] = input[line_idx].split(" ")
    return input


def get_hands_types(hands):
    for hand_idx in range(len(hands)):
        card_count = len(Counter(hands[hand_idx][0]))
        if card_count == 5:
            hands[hand_idx].append(7)
        elif card_count == 4:
            hands[hand_idx].append(6)
        elif card_count == 3:
            if max(Counter(hands[hand_idx][0]).values()) == 2:
                hands[hand_idx].append(5)
            else:
                hands[hand_idx].append(4)
        elif card_count == 2:
            if max(Counter(hands[hand_idx][0]).values()) == 3:
                hands[hand_idx].append(3)
            else:
                hands[hand_idx].append(2)
        else:
            hands[hand_idx].append(1)
    return hands


def get_hands_types_joker(hands):
    for hand_idx in range(len(hands)):
        joker_mode = 0
        for char_idx in range(len(hands[hand_idx][0])):
            if hands[hand_idx][0][char_idx] == 'J':
                joker_mode += 1
        if joker_mode == 0:
            card_count = len(Counter(hands[hand_idx][0]))
            if card_count == 5:
                hands[hand_idx].append(7)
            elif card_count == 4:
                hands[hand_idx].append(6)
            elif card_count == 3:
                if max(Counter(hands[hand_idx][0]).values()) == 2:
                    hands[hand_idx].append(5)
                else:
                    hands[hand_idx].append(4)
            elif card_count == 2:
                if max(Counter(hands[hand_idx][0]).values()) == 3:
                    hands[hand_idx].append(3)
                else:
                    hands[hand_idx].append(2)
            else:
                hands[hand_idx].append(1)
        else:
            card_count = Counter(hands[hand_idx][0])
            card_count.pop('J')
            if not card_count:
                hands[hand_idx].append(1)
                continue
            card_count[max(card_count, key=card_count.get)] += joker_mode
            card_count_len = len(card_count)
            if card_count_len == 5:
                hands[hand_idx].append(7)
            elif card_count_len == 4:
                hands[hand_idx].append(6)
            elif card_count_len == 3:
                if max(card_count.values()) == 2:
                    hands[hand_idx].append(5)
                else:
                    hands[hand_idx].append(4)
            elif card_count_len == 2:
                if max(card_count.values()) == 3:
                    hands[hand_idx].append(3)
                else:
                    hands[hand_idx].append(2)
            else:
                hands[hand_idx].append(1)
    return hands


def sort_by_type(x):
    return x[2]


def sort_by_card(hands):
    for hand_idx in range(len(hands)):
        hands[hand_idx][0] = list(map(map_char_to_int, list(hands[hand_idx][0])))
        hands[hand_idx][1] = int(hands[hand_idx][1])
    hands_sorted = sorted(hands, key=lambda x: (x[0][0], x[0][1], x[0][2], x[0][3], x[0][4]))
    for hand_idx in range(len(hands_sorted)):
        hands_sorted[hand_idx][0] = list(
            map(lambda x: map_char_to_int(x, reverse=1), hands_sorted[hand_idx][0]))
    return hands_sorted


def sort_by_card_joker(hands):
    for hand_idx in range(len(hands)):
        hands[hand_idx][0] = list(map(map_char_to_int_joker, list(hands[hand_idx][0])))
        hands[hand_idx][1] = int(hands[hand_idx][1])
    hands_sorted = sorted(hands, key=lambda x: (x[0][0], x[0][1], x[0][2], x[0][3], x[0][4]))
    for hand_idx in range(len(hands_sorted)):
        hands_sorted[hand_idx][0] = list(
            map(lambda x: map_char_to_int_joker(x, reverse=1), hands_sorted[hand_idx][0]))
    return hands_sorted


if __name__ == '__main__':
    input = parse_input("input.txt")
    # part 1
    hands = get_hands_types(input)

    hands.sort(key=sort_by_type)
    ones = list(filter(lambda x: x[2] == 1, hands))
    twos = list(filter(lambda x: x[2] == 2, hands))
    threes = list(filter(lambda x: x[2] == 3, hands))
    fours = list(filter(lambda x: x[2] == 4, hands))
    fives = list(filter(lambda x: x[2] == 5, hands))
    sixs = list(filter(lambda x: x[2] == 6, hands))
    sevens = list(filter(lambda x: x[2] == 7, hands))
    # filter by high card
    hands = []
    hands.extend(sort_by_card(sevens))
    hands.extend(sort_by_card(sixs))
    hands.extend(sort_by_card(fives))
    hands.extend(sort_by_card(fours))
    hands.extend(sort_by_card(threes))
    hands.extend(sort_by_card(twos))
    hands.extend(sort_by_card(ones))
    winnings = []
    for i in range(len(hands)):
        hands[i][2] = (i + 1) * hands[i][1]
        winnings.append(hands[i][2])
    total_winnings = sum(winnings)
    print(f"Total winnings part 1: {total_winnings}")

    # part 2
    input = parse_input("input.txt")
    hands = get_hands_types_joker(input)
    hands.sort(key=sort_by_type)
    ones = list(filter(lambda x: x[2] == 1, hands))
    twos = list(filter(lambda x: x[2] == 2, hands))
    threes = list(filter(lambda x: x[2] == 3, hands))
    fours = list(filter(lambda x: x[2] == 4, hands))
    fives = list(filter(lambda x: x[2] == 5, hands))
    sixs = list(filter(lambda x: x[2] == 6, hands))
    sevens = list(filter(lambda x: x[2] == 7, hands))
    # filter by high card
    hands = []
    hands.extend(sort_by_card_joker(sevens))
    hands.extend(sort_by_card_joker(sixs))
    hands.extend(sort_by_card_joker(fives))
    hands.extend(sort_by_card_joker(fours))
    hands.extend(sort_by_card_joker(threes))
    hands.extend(sort_by_card_joker(twos))
    hands.extend(sort_by_card_joker(ones))
    print(f"Hands: {hands}")
    winnings = []
    for i in range(len(hands)):
        hands[i][2] = (i + 1) * hands[i][1]
        winnings.append(hands[i][2])
    total_winnings = sum(winnings)
    print(f"Total winnings part 2: {total_winnings}")
