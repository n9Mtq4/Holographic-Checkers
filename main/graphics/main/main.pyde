#global stuff!!!!
pieceList = []
numPieces = 24

#current player flag
player = "B"

pieceWidth = (500)/8 #intuitive; the screen dimensions, three boards across the screen, 8 pieces across a board


# initialize the board as a double array with none values in each space
board = [None] * 8
for i in range(8):
    board[i] = [None] * 8



#gamerule check
#only need to update some positions, dont iterate them all
#def updatePiecePos(piece):
    
"""
# checker class has parameters team ("red" or "black"), x, y (ints) 
# methods 
"""
class Checker:
    team = ""
    x = 0
    y = 0
    king = False
    def __init__(self, team, x, y):
        self.team = team
        self.x = x
        self.y = y


def boardSetup():
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
                    board[i][j] = None
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
                    board[i][j] = None
        # middle part of board with no checkers
        else:
            # make the space empty
            for j in range(8):
                board[i][j] = None
                
    
# FUNCTION list of checkers iterated over, passed to drawPiece
#Makes an arr and calls to draw a new piece, an "update" if you will, to that piece  
def drawBoard(board):
    if player == "B":
        temp = []
        for i in range(0,4):
            # here I want to reverse the first list of the board (rows)
            temp = board[i]
            board[i] = board[7 - i]
            board[7 - i] = temp
    #white
    else:
        # here I want to reverse the second list of the board (cols)
        for i in range(0,8):
            temp = []
            for j in range(0,4):
                temp = board[i][j]
                board[i][j] = board[i][7 - j]
                board[i][7 - j] = temp
                
# draws anything in the board that isnt None
    for y in range(0,8):
        for x in range(0,8):
            if board[y][x]:
                board[y][x].x = x
                board[y][x].y = y
                drawPiece(board[y][x])
               
        


#okay, now this is epic. This function, like, totally draws a red or black sprite at the right position. It takes a checker object as input. Rad!
def drawPiece(checker):
    if checker.team == "B":
        #currPiece = blackPiece
        fill(0,0,0)
    else:
        #currPiece = redPiece
        fill(255,0,0)
    #image(currPiece, checker.x, checker.y)
    ellipse(checker.y*pieceWidth+(pieceWidth/2), checker.x*pieceWidth+(pieceWidth/2), pieceWidth, pieceWidth)



#################################################Setup thing is super important
def setup():
    size(500,500)
    background(100)
    frameRate(30)
    fill(255,0,0)
    #blackPiece = loadImage("black.jpg")
    #redPiece = loadImage("red.jpg")
    
    boardSetup()
    #instantiatePieceList()
    
#################################################Main draw loop
def draw():
    background(100) #gonna be a picture of a board
    drawBoard(board)
    
        
    
    
    
    
