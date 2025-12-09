with open("input.txt", "r") as input_file:
    result = 0

    for line in input_file:
        line = line.strip()
        n = len(line)

        index = -1
        indexes = []    
        
        result_length = 12
        intervall_limit = result_length

        while len(indexes) < 12:
            intervall_limit -= 1
            intervall_top = n - intervall_limit
            intervall_bottom = index
            
            max_value = 0
            for i in range(intervall_bottom + 1, intervall_top):
                if(int(line[i]) > max_value):
                    max_value = int(line[i])
                    index = i
            indexes.append(index)

        add_result_str = ""

        for j in indexes:
            add_result_str += line[j]

        result += int(add_result_str.strip())

with open("output_par2.txt", "w") as output_file:
    output_file.write(str(result))