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

    for i in range(len(input_lines)):
        for j in range(len(input_lines[i])):
            neighbors = 0

            if(input_lines[i][j] == 1):
                for k in adds:
                    try:
                        if((i+k[0] >= 0) and (j+k[1] >= 0) and(input_lines[i+k[0]][j+k[1]] == 1)):
                                neighbors += 1
                    except IndexError:
                        continue
                if(neighbors <= 3):
                    result += 1

with open("output_par1.txt", "w") as output_file:
    output_file.write(str(result))


            




                


