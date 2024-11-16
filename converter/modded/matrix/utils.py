class GameList(list):
    def __str__(self) -> str:
        return super().__str__()
    def syntaxStr(self) -> str:
        return f"GameList({self})"
    def show(self):
        result = ""
        for row in self:
            result += "\n" + "".join(row)
        return result

def create_matrix(width, height):
    matrix = []
    counter = 1

    for _ in range(height):
        row = [" " for i in range(width)]
        matrix.append(row)
        counter += width
    return GameList(matrix).syntaxStr()