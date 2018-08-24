'''Tic Tac Toe Game'''
def value(sett):
    """Tocheck x and o are present"""
    if 'x' in sett:
        return 'x'
    return 'o'

def play_game(game):
    '''Play game function'''
    seta = set()
    setb = set()
    setc = set()
    setd = set()
    sete = set()
    length = len(game)
    for index in range(length):
        for jindex in range(len(game[index])):
            if index == jindex:
                seta.add(game[index][jindex])
            if index + jindex == (len(game)-1):
                setb.add(game[index][jindex])
            fset = set(game[index])
            if len(fset) == 1:
                if 'x' in fset:
                    return 'x'
                return 'o'
            if jindex == 0:
                setc.add(game[index][jindex])
            if jindex == 1:
                setd.add(game[index][jindex])
            if jindex == 2:
                sete.add(game[index][jindex])
    if len(seta) == 1:
        return value(seta)
    if len(setb) == 1:
        return value(setb)
    if len(setc) == 1:
        return value(setc)
    if len(setd) == 1:
        return value(setd)
    if len(sete) == 1:
        return value(sete)
    return "draw"

def validation(game):
    '''Validating the players'''
    ele_x = 'x'
    ele_o = 'o'
    count_x = 0
    count_o = 0
    count_d = 0
    for index in game:
        if len(index) != 3:
            return "invalid game"
        if ele_x in index:
            count_x += index.count(ele_x)
        if ele_o in index:
            count_o += index.count(ele_o)
        if '.' in index:
            count_d += index.count('.')
    if count_x + count_o + count_d != 9:
        return "invalid input"
    if abs(count_x - count_o) != 1:
        return "invalid game"
    return play_game(game)

def main():
    '''Main function'''
    row = []
    for _ in range(3):
        col = input()
        col = list(map(str, col.split(' ')))
        row.append(col)
    row = validation(row)
    print(row)

if __name__ == '__main__':
    main()
