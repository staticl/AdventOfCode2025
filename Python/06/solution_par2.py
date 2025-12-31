from math import prod

with open("input.txt", "r") as input_file:
    result = 0
    lines = []
    column_nums = []

    for line in input_file:
        lines.append(line)

    rows = len(lines)
    columns = len(lines[0]) - 1

    operator = ""

    for j in range(columns):
        nums = ""
        for i in range(rows):
            if lines[i][j] == "+" or lines[i][j] == "*":
                operator = lines[i][j]
            elif lines[i][j] != " " and lines[i][j] != "\n":
                nums += lines[i][j]
        if nums == "" or j == columns - 1:
            if j == columns - 1:
                column_nums.append(nums)
            add_result = 0
            for num in column_nums:
                if add_result == 0:
                    add_result += int(num)
                elif operator == "+":
                    add_result += int(num)
                else:
                    add_result *= int(num)
            result += add_result
            column_nums = []
        else:
            column_nums.append(nums.strip())

with open("output_par2.txt", "w") as output_file:
    output_file.write(str(result))
