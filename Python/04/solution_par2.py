with open("input.txt", "r") as input_file:
    input_lines = []
    adds = [[-1, -1], [-1, 0], [-1, 1], [0, -1],
            [0, 1], [1, -1], [1, 0], [1, 1]]
    result = 0

    for line in input_file:
        line = line.strip()
        input_line = []

        for char in line:
            if (char == "@"):
                input_line.append(1)
            else:
                input_line.append(0)

        input_lines.append(input_line)

    input_lines_copy = list(input_lines)
    added_result = 1

    while added_result != 0:
        added_result = 0

        for i in range(len(input_lines)):
            for j in range(len(input_lines[i])):
                neighbors = 0

                if (input_lines[i][j] == 1):
                    for k in adds:
                        if ((0 <= i + k[0] <= len(input_lines) - 1) and (0 <= j + k[1] <= len(input_lines[i]) - 1) and (input_lines[i + k[0]][j + k[1]] == 1)):
                            neighbors += 1

                    if (neighbors <= 3):
                        input_lines_copy[i][j] = 0
                        added_result += 1

        result += added_result
        input_lines = list(input_lines_copy)

with open("output_par2.txt", "w") as output_file:
    output_file.write(str(result))
