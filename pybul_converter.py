from utils import *

from converter.vanilla.main import *
from converter.modded.main import *

from converter.libraries.main import *

from converter.modded.matrix.utils import GameList

from dataTypes.whithin_function_block import Whithin_function_block
import random
import time
import os
import keyboard

def func(custom_func):
    return lambda line: custom_func(line)

FUNC_BLOCK_HANDLERS =  {
    'клавиатура:': lambda obj: ON_PRESS(obj)
}

BULGARIAN_KEYWORDS = {
    'ако': func(IF),
    'кажи': func(PRINT),
    'друго:': func(ELSE),
    'попитай': func(INPUT),
    'или': func(ELIF),
    'случайно': func(RANDOM_NUMBER),
    'за': func(FOR),
    'направи': func(FOR),
    'спри': func(BREAK),
    'докато': func(WHILE),
    'и': lambda line: line.replace(' и ', ' and '),
    'игралноПоле': func(GAME_MAP),
    'покажи': func(SHOW),
    'завинаги:': lambda line: line.replace('завинаги:', 'while True:'),
    'изчакай': func(TIME_SLEEP),
    'изчисти': lambda line: line.replace('изчисти', "os.system('cls')"),
    'клавиатура:': lambda line: line,
    'съобщение': func(TKINTER_MESSAGE)
}

FUNCTION_WHITHIN_ITEMS = ['клавиатура:']


def custom_translate(file_path, snapshot=False, exec_script=True):
    with open(f"{file_path}/demo.pybul", 'r', encoding='utf-8') as file:
        code = file.readlines()

    translated_code = []
    whithin_function_block = Whithin_function_block()

    for line in code:
        line_converted = line
        keywords_for_convert = []
        line_items = line.split()
        
        for keyword in list(BULGARIAN_KEYWORDS.keys()):
            if keyword not in line_items:
                continue

            if keyword in FUNCTION_WHITHIN_ITEMS:
                if whithin_function_block.is_active():
                    raise RuntimeError(f"Не може да имаш функцич: {keyword} в кода на функция: {whithin_function_block['keyword']}")
                
                whithin_function_block = Whithin_function_block(keyword, count_indents(line)+4, '', line)
                continue

            keywords_for_convert.append(keyword)

        for keyword in keywords_for_convert:
            line_converted = BULGARIAN_KEYWORDS[keyword](line_converted)

        if whithin_function_block.is_active() and line != whithin_function_block.trigger_line:
            if count_indents(line) < whithin_function_block.indents:
                result = FUNC_BLOCK_HANDLERS[whithin_function_block.keyword](whithin_function_block)
                whithin_function_block.clear()
                translated_code.append(result)
                continue

            whithin_function_block.code += line_converted + "\n"
            continue

        if line.strip() and whithin_function_block.trigger_line != line:
            translated_code.append(line_converted)
    
    translated_code = "\n".join(translated_code)
    if snapshot:        
        with open(f"{file_path}/snapshot.py", "w", encoding="utf-8") as file:
            file.write(translated_code)
    
    if exec_script:
        exec(translated_code)
    
    return translated_code

custom_translate('./', True, True)
# custom_translate('./tests/code/simple', True)
