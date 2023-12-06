numbers_as_strings = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
numbers_as_strings_to_replace = ['o1e', 't2o', 't3e', 'f4r', 'f5e', 's6x', 's7n', 'e8t', 'n9e']


def parse_input(file_name):
    with open(file_name, 'r') as file:
        codes = file.read().splitlines()
    return codes


def replace_with_numerical(codes):
    numerical_codes = []
    for code in codes:
        for i in range(len(numbers_as_strings)):
            code = code.replace(numbers_as_strings[i], numbers_as_strings_to_replace[i])
        numerical_codes.append(code)
    return numerical_codes


def extract_calibration_value(code):
    calibration_value_string = ""
    calibration_value = list(filter((lambda x: 48 <= ord(x) <= 57), code))
    if len(calibration_value) >= 2:
        calibration_value_string += (calibration_value[0])
        calibration_value_string += (calibration_value[-1])
    else:
        calibration_value_string += calibration_value[0]
        calibration_value_string += calibration_value[0]
    return int(calibration_value_string)


if __name__ == '__main__':
    initial_codes = parse_input("input.txt")

    codes_numerical_only = []
    for line in initial_codes:
        codes_numerical_only.append(extract_calibration_value(line))
    print(f"Part 1: {sum(codes_numerical_only)}")

    initial_codes = replace_with_numerical(initial_codes)
    codes_numerical_only = []
    for line in initial_codes:
        codes_numerical_only.append(extract_calibration_value(line))
    print(f"Part 2: {sum(codes_numerical_only)}")
