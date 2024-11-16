def TIME_SLEEP(line):
    line_items = line.split(" ")
    index = line_items.index("изчакай")
    line_items[index] = f"time.sleep({line_items[index+1]})"
    for i in range(2):
        del line_items[index+1]
    return " ".join(line_items)