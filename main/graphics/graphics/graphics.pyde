#global stuff!!!!
pieceList = []
numPieces = 24

pieceWidth = (500/3)/8 #intuitive; the screen dimensions, three boards across the screen, 8 pieces across a board

board = [[x for x in range(8)]for y in range(8)]



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


        
    # give you three guesses what this does (it makes the pieces and  puts them in a list, dumbass)
# wipes the list, creates the first numPieces/2 (12?) pieces as black, then the rest as red
def instantiatePieceArray():
    #clear the list (.clear() isnt in processing?)
    pieceList = []
    for i in range(0,numPieces/2):
        if i%2==0:
            pieceList.append(Checker("black", i, 2))
        pieceList.append(Checker("black", i,i%2))#this does a fun thing to stagger the drawing, dont ask me to repeat it or explain it
    for a in range((numPieces/2)+1,numPieces-1):
        pieceList.append(Checker("red", i-12, 7-((i-12)%2)+1))
        if i%2==0:
            pieceList.append(Checker("red", i-12, 6))
    
#Makes an arr and calls to draw a new piece, an "update" if you will, to that piece  
def drawBoard (arr [][])
#checks for any 'None' values on the board
    for checkers in arr(checkersA):
        for checkers2 in arr(checkersB):
        
            if checkers2 == None:
               continue
           else 
               drawPiece(checkers2)
            

        #draw functions
#okay, now this is epic. This function, like, totally draws a red or black sprite at the right position. It takes a checker object as input. Rad!
def drawPiece(checker):
    if checker.team == "black":
        currPiece = blackPiece
        fill(0,0,0)
    else:
        currPiece = redPiece
        fill(255,0,0)
    #image(currPiece, checker.x, checker.y)
    ellipse(checker.x*pieceWidth, checker.y*pieceWidth, 20, 20)

#################################################Setup thing is super important
def setup():
    size(500,500)
    frameRate(30)
    
    blackPiece = loadImage("black.jpg")
    redPiece = loadImage("red.jpg")
    
    instantiatePieceArray()
    
    
    
#################################################Main draw loop
def draw():
    background(100) #gonna be a picture of a board
    for piece in pieceList:
        drawPiece(piece)
        print(String(piece.x))
    
        
    
    
    
    
    
