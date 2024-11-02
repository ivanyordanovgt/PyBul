def FOR_EACH(line):
    line = line.replace('всеки', '')

    if 'в' not in line:
        raise SyntaxError(f"Ключоша дума 'в' липсва в реда: {line}!")

    return line.replace(' в ', 'in')


def FOR_RANGE(line):
    line_items = line.split(' ')
    return f"for i in range( {line_items[1]} ):"


def FOR(line):
    line_items = line.split(' ')

    if "направи" in line_items:
        return FOR_RANGE(line)
    elif "за":
        return FOR_EACH(line)
