def RANDOM_NUMBER(line):
    line_items = line.split(' ')
    expression_start = line_items.index('случайно')

    if "от" in line and 'до' not in line:
        raise Exception("Когато имате командада 'от' при проиволно число, трябва да сложите до!")
    elif 'до' in line and 'от' not in line:
        raise Exception("Когато имате командада 'до' при случайно число, трябва да сложите от!")

    if "от" not in line:
        a, b = 0 , 10
        expression_end = line_items.index('число')
    else:
        expression_end = line_items.index('до') + 1
        a = line_items[line_items.index('от')+1]
        b = line_items[line_items.index('до')+1]

    line_items[expression_start] = f"random.randint({a}, {b})"
    del line_items[expression_start+1:expression_end + 1]

    return " ".join(line_items)
