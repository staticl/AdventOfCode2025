with open("input.txt", "r") as input_file:
    input_str = input_file.readline()
    input_str = input_str.split(sep = ",")

    result = 0

    for ranges in input_str:
        ranges = ranges.split(sep = "-")
        for i in range(int(ranges[0]), int(ranges[1])):
            num_length = len(str(i))
            if(num_length % 2 == 0):
                num_length_half = num_length // 2
                half_string = i % (pow(10, num_length_half))
                if (int(str(half_string) + str(half_string)) == i):
                    result += i

with open("output_par1.txt", "w") as output_file:
    output_file.write(str(result))