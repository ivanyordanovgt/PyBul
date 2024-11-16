from converter.modded.matrix.utils import create_matrix
from utils import count_indents
def GAME_MAP(line):
    indents = count_indents(line)
    line_items = line.split()
    keyword_index = line_items.index('игралноПоле')
    width, height = line_items[keyword_index+1].split("x")
    line_items[keyword_index] = str(create_matrix(int(width), int(height)))
    line_items[keyword_index+1] = ''
    return " "*indents + " ".join(line_items)