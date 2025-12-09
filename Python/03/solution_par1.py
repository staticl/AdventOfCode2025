with open("input.txt", "r") as input_file:
    result = 0

    for line in input_file:
        line = line.strip()
        n = len(line)

        index = -1
        indexes = []

        result_length = 2
        intervall_limit = result_length

        while len(indexes) < result_length:
            intervall_limit -= 1
            max_value = 0
            for i in range(index + 1, n - intervall_limit):
                if(int(line[i]) > max_value):
                    max_value = int(line[i])
                    index = i
            indexes.append(index)

        add_result_str = ""

        for j in indexes:
            add_result_str += line[j]

        result += int(add_result_str.strip())

with open("output_par1.txt", "w") as output_file:
    output_file.write(str(result))