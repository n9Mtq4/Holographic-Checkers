#global stuff!!!!
from com.n9mtq4.checker import CheckerWebsocketServer

port = 8881  # the port of the server

pieceList = []
numPieces = 24


#am i executing a turn? flag
flag = False

validMove = ''

#current player flag
player = "b"

pieceWidth = 80 #intuitive; the screen dimensions, three boards across the screen, 8 pieces across a board THIS NEEDS TO BE 45 FOR THE PROJECTOR

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
                    board[y][x] = Checker("b",y,x)
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
                    board[y][x] = Checker("r",y,x)
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

def updateBoard(move):
    board[int(move[3])][int(move[2])] = board[int(move[1])][int(move[0])] 
    board[int(move[1])][int(move[0])] = None #this is the piece being moved
    board[int(move[3])][int(move[2])].x = int(move[2])
    board[int(move[3])][int(move[2])].y = int(move[3])
   
def displayBoard(board, team):
    if team == 'b':
        line = ''
        for y in range(0,8):
            for x in range(0,8):
                if isinstance(board[7-y][x],Checker):
                    line += board[7-y][x].toString()
                else:
                    line += "0"
        drawBoard(line)
        #send string to phone
    # white player orientation
    elif team == 'r':
        line = ''
        for y in range(0,8):
            for x in range(0,8):
                if isinstance(board[y][7-x],Checker):
                    line += board[y][7-x].toString()
                else:
                    line += "0"
        drawBoard(line)
    else:
        print("invalid flag (its gotta be r or b)")


 
# draws anything in the board that isnt None
def drawBoard(output): #called with the flipped string
    print(output)
    x=0
    y=0
    for i in range(0,64):
        if i%8==0 and i != 0:
            y+=1
            x=0
        if (output[i] != "0"): #if there is a piece there, draw it
            drawPiece(y,x,output[i])
        x+=1
            #print(output[i])
               
    

#okay, now this is epic. This function, like, totally draws a red or black sprite at the right position. It takes a checker object as input. Rad!
def drawPiece(y,x,team):
    if team == "b":
        currPiece = bluePiece
    elif team == "B":
        currPiece = blueKing
    elif team == "r":
        currPiece = redPiece
    elif team == "R":
        currPiece = redKing
    else:
        print("kill myself") #helpful advice
    image(currPiece, x*pieceWidth, y*pieceWidth, pieceWidth, pieceWidth)
    #ellipse(x*pieceWidth+(pieceWidth/2), y*pieceWidth+(pieceWidth/2), pieceWidth, pieceWidth)



#################################################Setup thing is super important
def setup():
    size(pieceWidth*8, pieceWidth*8)
    background(100)
    frameRate(10)
    #noLoop()
    fill(255,255,255)
    global bluePiece
    bluePiece = loadImage("blue.png")
    global redPiece
    redPiece = loadImage("red.png")
    global backImg
    backImg = loadImage("checkerboard.png")
    
    boardSetup()# populates the starting board and pieces, array[][]

    frame = 0
    
    print("hello")
    #delay(5000)
#################################################Main draw loop
def draw():
    if flag:
        turn(validMove, nextPlayer)





def turn(move, nextTeam):
    image(backImg, 0, 0, pieceWidth*8, pieceWidth*8) #gonna be a picture of a board
    updateBoard(move)
    displayBoard(board, nextTeam)
    flag = false
    

    
