def ELIF(line):
    line_converted = line.replace('или ако', 'elif')
    line_converted = line_converted.replace('или', 'or')
    line_converted = line_converted.replace(' е ', ' == ')
    return line_converted