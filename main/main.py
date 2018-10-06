if __name__ == '__main__':
    class Checker:
        team = ""
        x = 0
        y = 0

        def __init__(self, team, x, y):
            self.team = team
    # initialize the board as a double array with none values in each space
    board = [None] * 8
    for i in range(8):
        board[i] = [None] * 8

    # add the checkers to each space properly for pregame setup
    for i in range(8):
        # lower part of board being initialized
        if i in range(0,3):
            for j in range(8):
                # if the space coordinates added together are divisible by 2
                # a checker should be placed on that coordinate
                if (i + j) % 2 == 0:
                    # TODO add a checker here properly instead of an empty string
                    board[i][j] = 'B'
                # make the space empty
                else:
                    board[i][j] = '0'
        # upper part of board being initialized
        elif i in range(5,8):
            for j in range(8):
                # if the space coordinates added together are divisible by 2
                # a checker should be placed on that coordinate
                if (i + j) % 2 == 0:
                    # TODO add a checker here properly instead of an empty string
                    board[i][j] = 'W'
                # make the space empty
                else:
                    board[i][j] = '0'
        # middle part of board with no checkers
        else:
            # make the space empty
            for j in range(8):
                board[i][j] = '0'
    # print out the board setup for testing. Comment this out if the above code is fully tested
    for i in range(0,8):
        line = " "
    # loop over the indices backwards so that the actual printout reflects the ordering of the board
    # bottom of the board should be 0,0 both under the hood and in the test printout
        for j in range(0,8):
            line += board[7-i][j] + " "
        print(line)