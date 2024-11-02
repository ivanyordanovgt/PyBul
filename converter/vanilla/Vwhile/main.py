def WHILE(line):
    line = line.replace(' e ', '==')
    return line.replace('докато', 'while')