with open("input.txt", "r") as input_file:
    result = 0

    input_ranges = []

    for line in input_file:
        if line == "\n":
            break
        else:
            line = line.strip()
            input_range = line.split("-")
            input_range[0] = int(input_range[0])
            input_range[1] = int(input_range[1])
            input_ranges.append(input_range)

    input_ranges = sorted(input_ranges)

    l = len(input_ranges)
    c = -1

    for r in input_ranges:
        range_end = r[1]
        if range_end > c:
            result += range_end - max(c, r[0] - 1)
            c = range_end

with open("output_par2.txt", "w") as output_file:
    output_file.write(str(result))
