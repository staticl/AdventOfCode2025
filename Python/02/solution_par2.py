with open("input.txt", "r") as input_file:
    input_str = input_file.readline()
    input_str = input_str.split(sep = ",")

    result = 0

    for ranges in input_str:
        ranges = ranges.split(sep = "-")
        for i in range(int(ranges[0]), int(ranges[1]) + 1):
            num_length = len(str(i))
            digit = ""
            for j in range((num_length) // 2):
                digit += str(i)[j]
                value_string = ""
                for k in range(num_length // len(digit)):
                    value_string += digit
                if(int(value_string) == i):
                    result += int(value_string)
                    break

with open("output_par2.txt", "w") as output_file:
    output_file.write(str(result))