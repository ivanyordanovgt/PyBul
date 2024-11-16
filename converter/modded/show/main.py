def SHOW(line):
    line_items = line.split(' ')

    keyword_index = line.index('покажи')
    line_converted = line[0:keyword_index] + f"print( {' '.join(line_items[keyword_index+1::])}.show() )"
    return line_converted