def INPUT(line):
    line_items = line.split('попитай')
    line = line.replace(line_items[-1], '')
    return line.replace("попитай", f"str(input({line_items[-1]}))")