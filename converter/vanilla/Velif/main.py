def ELIF(line):
    if "или ако" in line:
        line_converted = line.replace('или ако', 'elif')
    else:
        line_converted = line.replace('или', 'or')
    line_converted = line_converted.replace(' е ', ' == ')
    return line_converted