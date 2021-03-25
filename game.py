from random import randint
class Game():
    def __init__(self):
        self.boardx = 4
        self.boardy = 4
        self.board = [0 for i in range(self.boardx*self.boardy)]
        self.empties = []
        pass

    def printboard(self):
        print("###")
        for i in range(self.boardy):
            print("{}      {}      {}      {}".format(self.board[4*i-4],self.board[4*i-3],self.board[4*i-2], self.board[4*i-1]))
            print("")
        print("###")

    def addRandom(self):
        self.getEmpties()
        
        self.board[self.empties[randint(0,len(self.empties)-1)]]=2
    
    def getEmpties(self):
        self.empties = []
        for i in range(len(self.board)):
            if self.board[i]==0:
                self.empties.append(i)
        return self.empties
        
    def coordtoindx(self,x,y):
        return 4*y+x
    
    def indxtocoord(self, index):
        x = index%4
        y = int((index-x)/4)
        return x, y

myGame = Game()
for i in range(15):
    myGame.addRandom()
    myGame.printboard()