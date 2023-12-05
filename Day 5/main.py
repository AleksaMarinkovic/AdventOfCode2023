map_types = ['seed-to-soil map:', 'soil-to-fertilizer map:', 'fertilizer-to-water map:', 'water-to-light map:',
             'light-to-temperature map:', 'temperature-to-humidity map:', 'humidity-to-location map:']


def map_to_new_location(map, input):
    input_map = []
    output_map = []
    value = input
    for entry_idx in range(len(map)):
        input_map.append([map[entry_idx][1], map[entry_idx][1] + map[entry_idx][2] - 1])
        output_map.append([map[entry_idx][0], map[entry_idx][0] + map[entry_idx][2] - 1])
    for input_map_idx in range(len(input_map)):
        if input_map[input_map_idx][0] <= input <= input_map[input_map_idx][1]:
            value = output_map[input_map_idx][0] + input - input_map[input_map_idx][0]
    return value


def parse_input(file_name):
    with open(file_name, 'r') as file:
        input = file.read().splitlines()
        seeds = input[0]
        map_data = input[1:]
    seeds = seeds.replace("seeds: ", '')
    seeds = seeds.split(" ")
    for seed_idx in range(len(seeds)):
        seeds[seed_idx] = int(seeds[seed_idx])
    map_data.append('')
    separator_idxs = []
    for line_idx in range(len(map_data)):
        if map_data[line_idx] == '':
            separator_idxs.append(line_idx)
    maps = []
    for separator_idx in range(len(separator_idxs) - 1):
        maps.append(map_data[separator_idxs[separator_idx] + 2:separator_idxs[separator_idx + 1]])
    for map_idx in range(len(maps)):
        for entry_in_map_idx in range(len(maps[map_idx])):
            maps[map_idx][entry_in_map_idx] = maps[map_idx][entry_in_map_idx].split(" ")
            for value_idx in range(len(maps[map_idx][entry_in_map_idx])):
                maps[map_idx][entry_in_map_idx][value_idx] = int(maps[map_idx][entry_in_map_idx][value_idx])
    return seeds, maps


if __name__ == '__main__':
    seeds, maps = parse_input("input.txt")
    location_values = []
    # part 1
    for seed_idx in range(len(seeds)):
        value = seeds[seed_idx]
        for map_idx in range(len(maps)):
            value = map_to_new_location(maps[map_idx], value)
        location_values.append(value)
    print(min(location_values))

