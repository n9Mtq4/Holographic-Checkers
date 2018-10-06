

class Checker:
    team = ""
    x = 0
    y = 0

    def __init__(self, team, y, x):
        self.team = team

    def toString(self):
        return self.team

if __name__ == '__main__':
    # TODO fully implement this flag
    player = "B"
    # initialize the board as a double array with none values in each space
    board = [None] * 8
    for i in range(8):
        board[i] = [None] * 8

    # add the checkers to each space properly for pregame setup
    for i in range(8):
        # lower part of board being initialized (Black)
        if i in range(0,3):
            for j in range(8):
                # if the space coordinates added together are divisible by 2
                # a checker should be placed on that coordinate
                if (i + j) % 2 == 0:
                    # TODO add a checker here properly instead of an empty string
                    board[i][j] = Checker("B",i,j)
                # make the space empty
                else:
                    board[i][j] = '0'
        # upper part of board being initialized (White)
        elif i in range(5,8):
            for j in range(8):
                # if the space coordinates added together are divisible by 2
                # a checker should be placed on that coordinate
                if (i + j) % 2 == 0:
                    # TODO add a checker here properly instead of an empty string
                    board[i][j] = Checker("W",i,j)
                # make the space empty
                else:
                    board[i][j] = '0'
        # middle part of board with no checkers
        else:
            # make the space empty
            for j in range(8):
                board[i][j] = '0'




    # print out the board setup for testing. Comment this out if the above code is fully tested
    # black player orientation
    if player == "B":
        temp = []
        for i in range(0,4):
            # here I want to reverse the first list of the board (rows)
            temp = board[i]
            board[i] = board[7 - i]
            board[7 - i] = temp

    # white player orientation
    else:
        # here I want to reverse the second list of the board (cols)
        for i in range(0,8):
            temp = []
            for j in range(0,4):
                temp = board[i][j]
                board[i][j] = board[i][7 - j]
                board[i][7 - j] = temp

    for i in range(0,8):
        line = ' '
        for j in range(0,8):
            if isinstance(board[i][j],Checker):
                line += board[i][j].toString()
            else:
                line += board[i][j]
        print(line)

