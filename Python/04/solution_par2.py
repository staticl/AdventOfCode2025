with open("input.txt", "r") as input_file:
    input_lines = []
    adds = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
    result = 0    

    for line in input_file:
        line = line.strip()
        input_line = []

        for char in line:
            if(char == "@"):
                input_line.append(1)
            else:
                input_line.append(0)
        
        input_lines.append(input_line)

    input_lines_copy = list(input_lines)
    added_result = 1

    while added_result != 0:
        added_result = 0

        for i in range(len(input_lines[0])):
            for j in range(len(input_lines)):
                neighbors = 0
                if(input_lines[j][i] == 1):
                    for k in adds:
                        try:
                            if((j+k[0] >= 0) and (i+k[1] >= 0) and (input_lines[j+k[0]][i+k[1]] == 1)):
                                    neighbors += 1
                        except IndexError:
                            continue
                    if(neighbors <= 3):
                        input_lines_copy[j][i] = 0
                        added_result += 1
        
        result += added_result
        input_lines = list(input_lines_copy)

with open("output_par2.txt", "w") as output_file:
    output_file.write(str(result))