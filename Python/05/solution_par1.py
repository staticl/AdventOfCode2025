with open("input.txt", "r") as input_file:
    result = 0
    reader = True

    input_ranges = []

    for line in input_file:
        if reader == False:
            line = line.strip()
            for num_range in input_ranges:
                if int(line) in range(int(num_range[0]), int(num_range[1]) + 1):
                    result += 1
                    break

        if line == "\n":
            reader = False
            line = line.strip()

        if reader == True:
            input_range = line.split("-")
            input_ranges.append(input_range)

with open("output_par1.txt", "w") as output_file:
    output_file.write(str(result))
