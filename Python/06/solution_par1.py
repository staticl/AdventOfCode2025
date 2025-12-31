from math import prod

with open("input.txt", "r") as input_file:
    result = 0
    num_operations = []

    for line in input_file:
        line = line.strip()
        nums = line.split()
        num_operations.append(nums)

    columns = len(num_operations[0])
    rows = len(num_operations)

    for j in range(columns):
        column_nums = []
        for i in range(rows):
            if num_operations[i][j] != "+" and num_operations[i][j] != "*":
                column_nums.append(int(num_operations[i][j]))
            elif num_operations[i][j] == "+":
                result += sum(column_nums)
            else:
                result += prod(column_nums)

with open("output_par1.txt", "w") as output_file:
    output_file.write(str(result))
