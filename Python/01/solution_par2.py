import math

input = open("input.txt", "r")

code = 0
start = 50

for line in input:
    sign = 0
    num = ""
    
    for c in line:
        if(c == "R"):
            sign = 1
        elif(c == "L"):
            sign = -1
        else:
           num += c
    
    num = num.strip()

    old_start = start

    value = int(num)

    start += sign*(value % 100)

    if((old_start == 0)):
        code += (math.floor(value / 100))
    elif(start != 0):
        code += abs(math.floor(start / 100)) + (math.floor(value / 100))
    else:
        code += 1 + (math.floor(value / 100))

    if not (0 <= start < 100): 
        start += sign*(-1)*100
         

input.close()

output = open("output_par2.txt", "w")

output.write(str(code))

output.close()
