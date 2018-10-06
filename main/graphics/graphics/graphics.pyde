#global stuff!!!!
pieceList = []
numPieces = 24

pieceWidth = (1080/3)/8

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
            pieceList.append(Checker("red", i-12, 6)
    
    
# FUNCTION arraylist of checkers iterated over, passed to drawPiece


        #draw functions
#okay, now this is epic. This function, like, totally draws a red or black sprite at the right position. It takes a checker object as input. Rad!
def drawPiece(checker):
    if checker.team == "black":
        currPiece = blackPiece
    else:
        currPiece = redPiece
    #image(currPiece, checker.x, checker.y)
    ellipse(100,100,20,20)

#################################################Setup thing is super important
def setup():
    size(500,500)
    fill(100)
    blackPiece = loadImage("black.jpg")
    redPiece = loadImage("red.jpg")

    instantiatePieceArray()
    
    
    
#################################################Main draw loop
def draw():
    background(0) #gonna be a picture of a board
    for piece in pieceList:
        drawPiece(piece)
        
    
    
    
    
    
