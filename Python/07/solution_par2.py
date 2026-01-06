with open("input.txt", "r") as input_file:
    beam_list = []
    value_list = []

    for line in input_file:
        n = len(line) - 1
        i = 0
        if value_list == []:
            for j in range(n):
                value_list.append(0)
        for c in line:
            if c == "S":
                beam_list.append(i)
                value_list[i] = 1
            elif c == "^":
                if i in beam_list:
                    beam_list.remove(i)
                    if i + 1 not in beam_list:
                        beam_list.append(i + 1)
                    if i - 1 not in beam_list:
                        beam_list.append(i - 1)
                    value_list[i + 1] += value_list[i]
                    value_list[i - 1] += value_list[i]
                    value_list[i] = 0
            i += 1

    result = sum(value_list)

with open("output_par2.txt", "w") as output_file:
    output_file.write(str(result))
