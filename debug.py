print( "Добре дошъл!"
 )
отговор = str(input( "Готов да играем?"
))
if отговор == "не":

    print( "Добре тогава!"
 )
    while True:

        print( "Умри в кофа"
 )
        print( random.randint(1, 9999**999
) )
играчРед = 0 

играчКолона = 0

точки = 0

ябълкаРед = random.randint(1, 9
)
ябълкаКолона = random.randint(1, 4
)

def gcfoqexplektwrwjchzxeyguqkznkdrwybwrgcjsfyqpaiybxj(data):
    global играчРед, играчКолона

    if data.name == "а":

        играчКолона -= 1

    elif data.name == "с":

        играчРед += 1

    elif data.name == "ш":

        играчРед -= 1

    elif data.name == "д":

        играчКолона += 1

    else: 

        print( "друго"
 )

keyboard.on_press(gcfoqexplektwrwjchzxeyguqkznkdrwybwrgcjsfyqpaiybxj) 

while True:

    os.system('cls')

    полеЗаИгра = GameList([[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]) 
    полеЗаИгра[играчРед][играчКолона] = "x"

    полеЗаИгра[ябълкаРед][ябълкаКолона] = "A"

    if [играчРед, играчКолона] == [ябълкаРед, ябълкаКолона]:

        точки += 1

        ябълкаРед = random.randint(1, 9
)
        ябълкаКолона = random.randint(1, 4
)
    print( полеЗаИгра
.show() )
    print( f"Точки: {точки}"
 )
    time.sleep(0.1)