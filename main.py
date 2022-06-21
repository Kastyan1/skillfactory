def greet():
    print('Крестики - нолики')
    print('ввод координат: x, y, где х - номер строки, а y - номер столбца')
greet()

game_field = [
         [' ', ' ', ' '],
         [' ', ' ', ' '],
         [' ', ' ', ' ']
]

def show():
    print(f"   0  1  2")
    print(f' 0 {game_field[0][0]}, {game_field [0][1]}, {game_field [0][2]}')
    print(f' 1 {game_field[1][0]}, {game_field[1][1]}, {game_field[1][2]}')
    print(f' 2 {game_field[2][0]}, {game_field[2][1]}, {game_field[2][2]}')
show()


def step_player():
    while True:
        cords = input("Куда поставить: ").split()

        if len(cords) != 2:
            print("Введите 2 координаты! ")
            continue

        x, y = cords

        if not (x.isdigit()) or not (y.isdigit()):
            print("Введите числа! ")
            continue

        x, y = int(x), int(y)

        if x < 0 or x > 2 or y < 0 or y > 2:
            print(" Координаты вне диапазона (от 0 до 2)! ")
            continue

        if game_field[x][y] != " ":
            print(" Клетка занята другим игроком! ")
            continue

        return x, y
step_player()


def check_win():
    win_cord = (((0, 0), (0, 1), (0, 2)),  ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 0), (1, 1), (2, 2)), ((0, 2), (1, 1), (2, 0)),
                ((0, 0), (1, 0), (2, 0)), ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))

    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(game_field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("Выиграл 1 игрок (Х)!!!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выиграл 2 игрок (0)!!!")
            return True
    return False
check_win()

greet()
game_field = [
         [' ', ' ', ' '],
         [' ', ' ', ' '],
         [' ', ' ', ' ']
]
step = 0
while True:
    step += 1
    show()
    if step % 2 == 1:
        print('Ходит 1 игрок (X):')
    else:
        print('Ходит 2 игрок (0):')
    x, y = step_player()

    if step % 2 == 1:
        game_field[x][y] = 'X'
    else:
        game_field[x][y] = '0'
    if check_win():
        break
    if step == 9:
        print('Ничья!!!')
        break
