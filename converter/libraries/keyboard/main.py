from dataTypes.whithin_function_block import Whithin_function_block
from utils import create_function
"""
клавиатура при "x"
"""



def ON_PRESS(whithin_function_block: Whithin_function_block):
    line_items = whithin_function_block.trigger_line.split(" ")
    print(line_items)
    index = line_items.index("клавиатура:")
    name, code = create_function(whithin_function_block.code)
    result = code.replace('клавиш', 'data.name')
    result += f"keyboard.on_press({name})"
    line_items[index] = result
    
    return " ".join(line_items)