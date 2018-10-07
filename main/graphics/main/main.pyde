numPieces = 24

#am i executing a turn? flag

moves = ["2233", "3544", "1122", "7564", "6273", "0213", "4635", "3324", "1533", "3311", "0022", "2615", "4233", "6453", "3324", "1533", "3311", "2002", "1726", "3122", "3524", "1335", "3517", "5746", "1726", "4635", "2615", "0000"]
moveCounter = 0


okMove = "4253"
nextPlayer = "b"

#current player flag
player = "b"

pieceWidth = 45 #intuitive; the screen dimensions, three boards across the screen, 8 pieces across a board THIS NEEDS TO BE 45 FOR THE PROJECTOR

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

#just for testing kinging
"""
def boardSetup():
    for y in range(8):
        for x in range(8):
            board[y][x] = None
        board[6][1] = Checker("b", 1, 6)
        board[1][1] = Checker("r", 1, 1)

"""
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
    
    currPiece = board[int(move[3])][int(move[2])]
    currPiece.x = int(move[2])
    currPiece.y = int(move[3])
    x1=int(move[0])
    y1=int(move[1])
    x2=int(move[2])
    y2=int(move[3])
    deltaX = int(move[2])-int(move[0])
    deltaY = int(move[3])-int(move[1])
    
    

    if (abs(deltaX) > 1) or (abs(deltaY) > 1): #if the move is a jump, remove the piece jumped over
        board[y1+(deltaY/2)][x1+(deltaX/2)] = None
        # checking if the point it moved to would make it a king
    print("kinged?")

    if ((currPiece.team == "r") and (y2 == 0)):
        currPiece.team = "R"
        currPiece.king = True
    if ((currPiece.team == "b") and (y2 == 7)):
        currPiece.team = "B"
        currPiece.king = True
    
        
   
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
    # red player orientation
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
    #print(output) ############################################This would pass the string to the server function
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
               
    
#takes a checker object as input, draws it in the correct place
def drawPiece(y,x,team):
    if team == "b":
        currPiece = bluePiece
    elif team == "B": #hacking b
        currPiece = blueKing
    elif team == "r":
        currPiece = redPiece
    elif team == "R":
        currPiece = redKing
    else:
       print("error09") #helpful advice
    image(currPiece, x*pieceWidth+780, y*pieceWidth, pieceWidth, pieceWidth)



#################################################Setup thing is super important
def setup():
    size(1920,1040)
    background(0)
    frameRate(30)
    #noLoop()
    fill(255,255,255)
    global bluePiece
    bluePiece = loadImage("blue.png")
    global redPiece
    redPiece = loadImage("red.png")
    global blueKing
    blueKing = loadImage("blueKing.png")
    global redKing
    redKing = loadImage("redKing.png")
    global backImg
    backImg = loadImage("checkerboard.png")
    
    boardSetup()# populates the starting board and pieces, array[][]

    global flag
    flag = -1
    
    image(backImg, 780, 0, pieceWidth*8, pieceWidth*8) #picture of a board
    displayBoard(board, "b")
    #delay(5000)
#################################################Main draw loop
def draw():
    if flag==frameCount:
        turn(okMove, nextPlayer)


def turn(move, nextTeam):
    
    #flag = frameCount
    print("turn got called")
    image(backImg, 780, 0, pieceWidth*8, pieceWidth*8) #picture of a board
    updateBoard(move)
    print("board update worked")
    displayBoard(board, nextTeam)
    save("screen.jpg")
    img = loadImage("screen.jpg")
    #rotate(PI/2.0)
    image(img, 0, 680)

    
def keyTyped():
    print("typed %s %d" % (key, keyCode))
    global okMove
    global flag
    global nextPlayer
    global moves
    global moveCounter
    
    if key == "q":
        if dealWithString(moves[moveCounter]):
            okMove = moves[moveCounter]
            if moveCounter < len(moves):
                moveCounter += 1
            #nextPlayer = "b"
            flag = frameCount+1
    if key == "w":
        if dealWithString("2031"):
            okMove = "2031"
            nextPlayer = "b" 
            flag = frameCount+5



    
def dealWithString(string):
    #int x coordinate 1 
    xOne = int(string[0])
    yOne = int(string[1])
    xTwo = int(string[2])
    yTwo = int(string[3])
    return validMove(xOne, yOne, xTwo, yTwo)


def validMove(xOne, yOne, xTwo, yTwo):
    print(xOne)
    print(yOne)
    global board
    if (xOne>7) or (yOne>7) or (xTwo>7) or (yTwo>7) or (xOne<0) or (yOne<0) or (xTwo<0) or (yTwo<0):
        return False
    if board[yOne][xOne] == None:
        return False
    else:
        initial = board[yOne][xOne]
        deltaY = (yTwo-yOne)
        if (deltaY<0 and (initial.team == "b")) or (deltaY>0 and (initial.team == "r")):
            print("wrong deltaY for team")
            return False
        deltaX = (xTwo-xOne)
        if((abs(deltaX)!=2) or (abs(deltaY)!=2)):
            if((abs(deltaX)!=1) or (abs(deltaY)!=1)):
                return False
            elif board[yTwo][xTwo] == None:
                return True
            else:
                return False
        else:
            jumped = board[yOne+(deltaY/2)][xOne+(deltaX/2)]
            # if the target spot is empty and the spot to be jumped over has a checker and its team is different than the jumping piece's team
            if (board[yTwo][xTwo] == None) and (jumped != None) and (jumped.team.upper() != initial.team.upper()):  
                return True
            else:
                return False
