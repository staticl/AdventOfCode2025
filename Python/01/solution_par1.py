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

    value = int(num)

    start += sign*(value % 100)

    if not (0 <= start < 100): 
        start = start + sign*(-1)*100          
    
    if(start == 0):
        code += 1  


input.close()

output = open("output_par1.txt", "w")

output.write(str(code))

output.close()
