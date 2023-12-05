map_types = ['seed-to-soil map:', 'soil-to-fertilizer map:', 'fertilizer-to-water map:', 'water-to-light map:',
             'light-to-temperature map:', 'temperature-to-humidity map:', 'humidity-to-location map:']


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


def overlapping_nonoverlapping_range(ranges_x, ranges_y):
    total_overlapping_subranges = []
    total_non_overlapping_subranges = []
    for range_x_idx in range(len(ranges_x)):
        overlapping_subranges = []
        non_overlapping_subranges = []
        for range_y in ranges_y:
            start_x = ranges_x[range_x_idx][0]
            end_x = ranges_x[range_x_idx][1]
            start_y = range_y[0]
            end_y = range_y[1]
            if max(start_x, start_y) <= min(end_x, end_y):
                # overlapping - these subranges are getting mapped
                overlapping_subrange = [max(start_x, start_y), min(end_x, end_y)]
                overlapping_subranges.append(overlapping_subrange)
        # non overlapping - these subranges aren't getting mapped
        overlapping_subranges.sort()
        start = ranges_x[range_x_idx][0]
        for i in range(ranges_x[range_x_idx][0], ranges_x[range_x_idx][1], 1):
            for idx in range(len(overlapping_subranges)):
                if i == overlapping_subranges[idx][0]:
                    if start != overlapping_subranges[idx][0]:
                        non_overlapping_subranges.append([start, overlapping_subranges[idx][0]])
                    start = overlapping_subranges[idx][1]
        if start < ranges_x[range_x_idx][1]:
            non_overlapping_subranges.append([start, ranges_x[range_x_idx][1]])
        total_overlapping_subranges.extend(overlapping_subranges)
        total_non_overlapping_subranges.extend(non_overlapping_subranges)
    total_overlapping_subranges.sort()
    total_non_overlapping_subranges.sort()
    return total_overlapping_subranges, total_non_overlapping_subranges


if __name__ == '__main__':
    seeds, maps = parse_input("input.txt")
    new_seeds = []
    for idx in range(0, len(seeds) - 1, 2):
        new_seeds.append([seeds[idx], seeds[idx] + seeds[idx + 1]])

    x = new_seeds
    x.sort()
    i = 0
    for map in maps:
        if i == 1:
            break
        print("x: ")
        print(x)
        y = []
        for entry in map:
            y.append([entry[1], entry[1] + entry[2]])
        y.sort()
        print("y: ")
        print(y)
        subranges_to_map, subranges_to_continue = overlapping_nonoverlapping_range(x, y)
        print("subranges_to_map:")
        print(subranges_to_map)
        print("subranges_to_continue:")
        print(subranges_to_continue)
        # quit after 1 iteration until done with rest of implementation
        i += 1
        # mapped_subranges = []
        # for subrange in subranges_to_map:
        #    mapped_subranges.append()
