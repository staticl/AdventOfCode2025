with open("input.txt", "r") as input_file:
    result_code = 0
    position = 50

    for line in input_file:
        direction = 0
        number_str = ""

        for c in line:
            if (c == "R"):
                direction = 1
            elif (c == "L"):
                direction = -1
            else:
                number_str += c

        number_str = number_str.strip()
        value = int(number_str)

        position += direction * (value % 100)

        if not (0 <= position < 100):
            position += direction * (-1) * 100

        if (position == 0):
            result_code += 1


with open("output_par1.txt", "w") as output_file:
    output_file.write(str(result_code))
