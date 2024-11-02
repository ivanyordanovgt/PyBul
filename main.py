from converter.vanilla.Vif.main import IF
from converter.vanilla.Vprint.main import PRINT
from converter.vanilla.Velif.main import ELIF
from converter.vanilla.Velse.main import ELSE
from converter.vanilla.Vinput.main import INPUT
from converter.vanilla.Vfor.main import FOR
from converter.vanilla.Vbreak.main import BREAK
from converter.vanilla.Vwhile.main import WHILE
from converter.modded.random.number import RANDOM_NUMBER

import random

def func(custom_func):
    return lambda line: custom_func(line)

BULGARIAN_KEYWORDS = {
    'ако': func(IF),
    'кажи ': func(PRINT),
    'друго:': func(ELSE),
    'попитай': func(INPUT),
    'или': func(ELIF),
    'случайно ': func(RANDOM_NUMBER),
    'за ': func(FOR),
    'направи ': func(FOR),
    'спри': func(BREAK),
    'докато': func(WHILE),
    ' и ': lambda line: line.replace(' и ', ' and '),
    ' или ': lambda line: line.replace(' или ', ' or ')
}
def count_indents(line):
    c = 0
    for el in line:
        c += 1
        if el != ' ':
            return c
    return c
def custom_translate(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        code = file.readlines()

    translated_code = []

    for line in code:
        line_converted = line
        keywords_for_convert = []

        for keyword in list(BULGARIAN_KEYWORDS.keys()):
            if keyword in line:
                keywords_for_convert.append(keyword)

        for keyword in keywords_for_convert:
            line_converted = BULGARIAN_KEYWORDS[keyword](line_converted)

        if line.strip():
            translated_code.append(line_converted)

    exec('\n'.join(translated_code))


custom_translate('demo.txt')
