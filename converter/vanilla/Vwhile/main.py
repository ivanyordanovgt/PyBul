def WHILE(line):
    line = line.replace(' е ', ' == ')
    line = line.replace(' e ', ' == ')

    return line.replace('докато', 'while')