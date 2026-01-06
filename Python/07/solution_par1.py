with open("input.txt", "r") as input_file:
    result = 0
    beam_list = []

    for line in input_file:
        n = len(line) - 1
        i = 0
        for c in line:
            if c == "S":
                beam_list.append(i)
            elif c == "^":
                if i in beam_list:
                    beam_list.remove(i)
                    result += 1
                    if i == 0 and i + 1 not in beam_list:
                        beam_list.append(i + 1)
                    elif i == n and i - 1 not in beam_list:
                        beam_list.append(i - 1)
                    else:
                        if i + 1 not in beam_list:
                            beam_list.append(i + 1)
                        if i - 1 not in beam_list:
                            beam_list.append(i - 1)
            i += 1

with open("output_par1.txt", "w") as output_file:
    output_file.write(str(result))
