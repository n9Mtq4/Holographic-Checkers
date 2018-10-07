#global stuff!!!!
pieceList = []
numPieces = 24

#current player flag
player = "B"

pieceWidth = (500)/8 #intuitive; the screen dimensions, three boards across the screen, 8 pieces across a board


# initialize the board as a double array with none values in each space
board = [None] * 8
for y in range(8):
    board[y] = [None] * 8



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
    def toString(self):
        return self.team


def boardSetup():
    # add the checkers to each space properly for pregame setup
    for y in range(8):
        # lower part of board being initialized (Black)
        if y in range(0,3):
            for x in range(8):
                # if the space coordinates added together are divisible by 2
                # a checker should be placed on that coordinate
                if (y + x) % 2 == 0:
                    # TODO add a checker here properly instead of an empty string
                    board[y][x] = Checker("B",y,x)
                # make the space empty
                else:
                    board[y][x] = None
        # upper part of board being initialized (White)
        elif y in range(5,8):
            for x in range(8):
                # if the space coordinates added together are divisible by 2
                # a checker should be placed on that coordinate
                if (y + x) % 2 == 0:
                    # TODO add a checker here properly instead of an empty string
                    board[y][x] = Checker("W",y,x)
                # make the space empty
                else:
                    board[y][x] = None
        # middle part of board with no checkers
        else:
            # make the space empty
            for x in range(8):
                board[y][x] = None
                
    
# FUNCTION list of checkers iterated over, passed to drawPiece
#Makes an arr and calls to draw a new piece, an "update" if you will, to that piece 

def updateBoardList(move):
    board[move[3]][move[2]] = board[move[1]][move[0]] 
    board[move[1]][move[0]] = None #this is the piece being moved
    board[move[3]][move[2]].x = move[2]
    board[move[3]][move[2]].y = move[3]
   
def updateBoard(board):
    if player == 'B':
        line = ''
        for y in range(0,8):
            for x in range(0,8):
                if isinstance(board[7-y][x],Checker):
                    line += board[7-y][x].toString()
                else:
                    line += "0"
        drawBoard(line)
    # white player orientation
    if player == 'W':
        line = ''
        for y in range(0,8):
            for x in range(0,8):
                if isinstance(board[y][7-x],Checker):
                    line += board[y][7-x].toString()
                else:
                    line += "0"
        drawBoard(line)


 
# draws anything in the board that isnt None
def drawBoard(output): #called with the flipped string
    i=0
    for y in range(0,8):
        for x in range(0,8):
            if output[i] == "W" or "B":
                drawPiece(y,x,output[i])
            i+=1
            print(output[i])
               
    

#okay, now this is epic. This function, like, totally draws a red or black sprite at the right position. It takes a checker object as input. Rad!
def drawPiece(y,x,team):
    if team == "B":
        #currPiece = blackPiece
        fill(0,0,0)
    else:
        #currPiece = redPiece
        fill(255,0,0)
    #image(currPiece, checker.x, checker.y)
    ellipse(y*pieceWidth+(pieceWidth/2), x*pieceWidth+(pieceWidth/2), pieceWidth, pieceWidth)



#################################################Setup thing is super important
def setup():
    size(500,500)
    background(100)
    frameRate(1)
    fill(255,0,0)
    #blackPiece = loadImage("black.jpg")
    #redPiece = loadImage("red.jpg")
    
    boardSetup()
    #instantiatePieceList()
    
#################################################Main draw loop
def draw():
    background(100) #gonna be a picture of a board
    updateBoard(board)
    drawBoard(board)
    
        
    
    
    
    
