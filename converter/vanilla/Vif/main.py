def IF(line):
    line_items = line.split(' ')
    if line_items[line_items.index('ако')-1] == 'или':
        return line

    line_converted = line.replace('ако', 'if')
    line_converted = line_converted.replace(' е ', ' == ')
    return line_converted