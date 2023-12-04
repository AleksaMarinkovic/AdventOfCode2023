def is_char_digit(char):
    return 48 <= int(ord(char)) <= 57


def find_neighbouring_numbers(prev_line, line, next_line, index, part_numbers_exactly=-1):
    part_numbers = []
    # for line (current line)
    if is_char_digit(line[index - 1]):
        part_numbers.append(get_number_from_index(line, index - 1))
    if is_char_digit(line[index + 1]):
        part_numbers.append(get_number_from_index(line, index + 1))
    # for prev_line
    for idx in range(index - 1, index + 2, 1):
        if is_char_digit(prev_line[idx]):
            if get_number_from_index(prev_line, idx) not in part_numbers:
                part_numbers.append(get_number_from_index(prev_line, idx))
    # for next_line
    for idx in range(index - 1, index + 2, 1):
        if is_char_digit(next_line[idx]):
            if get_number_from_index(next_line, idx) not in part_numbers:
                part_numbers.append(get_number_from_index(next_line, idx))
    part_numbers_value = 0
    if part_numbers_exactly == -1:
        for part_number in part_numbers:
            part_numbers_value += int(part_number)
    else:
        if len(part_numbers) == part_numbers_exactly:
            part_numbers_value = 1
            for part in part_numbers:
                part_numbers_value *= int(part)
    return part_numbers_value


def get_number_from_index(line, index):
    if not is_char_digit(line[index]):
        return
    while index >= 0 and is_char_digit(line[index]):
        index -= 1
    index += 1
    output = ""
    while index < len(line) and is_char_digit(line[index]):
        output += line[index]
        index += 1
    return int(output)


def get_line_length(input):
    return len(input[0])


def extract_unique_symbols(input):
    output = []
    for line in input:
        for character in line:
            if character not in output:
                output.append(character)
    output = list(filter(lambda x: not is_char_digit(x), output))
    output.pop(output.index('.'))
    return output


def parse_input(file_name):
    with open(file_name) as file:
        input = file.read().splitlines()
        return input


if __name__ == '__main__':
    input = parse_input("input.txt")
    # use unique symbols for part one
    #unique_symbols = extract_unique_symbols(input)
    # use this for part two
    unique_symbols = ['*']
    line_length = get_line_length(input)
    total_sum = 0
    for line_idx in range(1, len(input) - 1, 1):
        for char_idx in range(len(input[line_idx])):
            if input[line_idx][char_idx] in unique_symbols:
                total_sum += find_neighbouring_numbers(input[line_idx - 1], input[line_idx], input[line_idx + 1],
                                                       char_idx,2)
    print(total_sum)