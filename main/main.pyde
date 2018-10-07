



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
    
        
    
    
    
    
