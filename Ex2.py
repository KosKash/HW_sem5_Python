# Крестики нолики консоль
cell = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def printer(cell: list):
    print(f'{cell[0]} | {cell[1]} | {cell[2]}')
    print('---------')
    print(f'{cell[3]} | {cell[4]} | {cell[5]}')
    print('---------')
    print(f'{cell[6]} | {cell[7]} | {cell[8]}')
win = False
printer(cell)
move = True
while win == False:
    if move == True:
        comeX = int(input('На какую клетку хотите поставить "Х"'))
        if cell[comeX - 1] != '0' and cell[comeX - 1] != 'X':
            cell[comeX-1] = 'X'
            move = False
        else:
            print('Try again')
        if (cell[0] ==  cell[1]  ==  cell[2] == 'X') or (cell[3] == cell[4] == cell[5] == 'X') or (cell[6] == cell[7] == cell[8] == 'X') or (cell[0] == cell[3] == cell[6] == 'X') or (cell[1] == cell[4] == cell[7] == 'X') or (cell[2] == cell[5] == cell[8] == 'X') or (cell[6] == cell[4] == cell[2] == 'X') or (cell[0] == cell[4] == cell[8] == 'X'):
            win = True
            print("X Win")
            break
        printer(cell)
    if move == False:
        come0 = int(input('На какую клетку хотите поставить "O"'))
        if cell[come0-1] != '0' and cell[come0-1] != 'X':
            cell[come0-1] = '0'
            move = True
        else:
            print('Try again')
        if (cell[0] ==  cell[1]  ==  cell[2] == '0') or (cell[3] == cell[4] == cell[5] == '0') or (cell[6] == cell[7] == cell[8] == '0') or (cell[0] == cell[3] == cell[6] == '0') or (cell[1] == cell[4] == cell[7] == '0') or (cell[2] == cell[5] == cell[8] == '0') or (cell[6] == cell[4] == cell[2] == '0') or (cell[0] == cell[4] == cell[8] == '0'):
            win = True
            print("0 Win")
            break
        printer(cell)
