class Whithin_function_block:
    def __init__(self, keyword='', indents='', code='', trigger_line=''):
        self.keyword = keyword
        self.indents = indents
        self.code = code
        self.trigger_line = trigger_line

    def clear(self):
        self.keyword = ''
        self.indents = 0
        self.code = ''
        self.trigger_line = ''

    def is_active(self):
        return self.keyword