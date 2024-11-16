import random

def count_indents(line):
    c = 0
    for el in line:
        if el != ' ':
            return c
        c += 1
    return c

def create_function(code: str, condition="") -> str:
    chars = 'qwertyuiopasdfghjklzxcvbnm'
    name = "".join([chars[random.randint(0, len(chars)-1)] for x in range(50)])
    if condition:
        code = f"""
    {condition}
    {code}
        """
    return name, f"""
def {name}(data):
{code}
"""

print(count_indents("    "))