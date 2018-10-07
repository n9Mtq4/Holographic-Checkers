

class Checker:
    team = ""
    x = 0
    y = 0

    def __init__(self, team, x, y):
        self.team = team

    def toString(self):
        return self.team

if __name__ == '__main__':
    # TODO fully implement this flag
    player = "W"
    # initialize the board as a double array with none values in each space
    board = [None] * 8
    for y in range(8):
        board[y] = [None] * 8

    # add the checkers to each space properly for pregame setup
    for y in range(8):
        # lower part of board being initialized (Black)
        if y in range(0, 3):
            for x in range(8):
                # if the space coordinates added together are divisible by 2
                # a checker should be placed on that coordinate
                if (y + x) % 2 == 0:
                    board[y][x] = Checker("B", x, y)
                # make the space empty
                else:
                    board[y][x] = '0'
        # upper part of board being initialized (White)
        elif y in range(5, 8):
            for x in range(8):
                # if the space coordinates added together are divisible by 2
                # a checker should be placed on that coordinate
                if (y + x) % 2 == 0:
                    board[y][x] = Checker("W", x, y)
                # make the space empty
                else:
                    board[y][x] = '0'
        # middle part of board with no checkers
        else:
            # make the space empty
            for x in range(8):
                board[y][x] = '0'




    # print out the board setup for testing. Comment this out if the above code is fully tested
    # black player orientation
    if player == "B":
        temp = []
        for y in range(0, 4):
            # here I want to reverse the first list of the board (rows)
            temp = board[y]
            board[y] = board[7 - y]
            board[7 - y] = temp

    # white player orientation
    else:
        # here I want to reverse the second list of the board (cols)
        for y in range(0, 8):
            temp = []
            for x in range(0, 4):
                temp = board[y][x]
                board[y][x] = board[y][7 - x]
                board[y][7 - x] = temp

    for y in range(0,8):
        line = ' '
        for x in range(0,8):
            if isinstance(board[y][x],Checker):
                line += board[y][x].toString()
            else:
                line += board[y][x]
        print(line)

