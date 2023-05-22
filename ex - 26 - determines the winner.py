game = [[2, 0, 2],
        [1, 0, 2],
        [1, 1, 2]]


def check_win(game):
    for row in game:
        if len(set(row)) == 1 and row[0] != 0:
            return row[0]
    for col in range(len(game)):
        if game[0][col] == game[1][col] == game[2][col] != 0:
            return game[0][col]
        if game[0][0] == game[1][1] == game[2][2] != 0:
            return game[0][0]
        if game[0][2] == game[1][1] == game[2][0] != 0:
            return game[0][2]


w = str(check_win(game))

if w:
    print(w + " " + "wins")
else:
    print("no winner")
