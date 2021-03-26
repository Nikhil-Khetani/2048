from random import randint
class Game():
    def __init__(self, human):
        self.boardx = 4
        self.boardy = 4
        self.board = [0 for i in range(self.boardx*self.boardy)]
        self.empties = []
        self.human = human
        pass

    def printboard(self):
        print("###")
        print("")
        for j in range(self.boardy):
            print("{}      {}      {}      {}".format(self.board[4*j],self.board[4*j+1],self.board[4*j+2], self.board[4*j+3]))
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

    def getPlayerInput(self):
        action = input()
    
    def step(self, action):
        pass

    def right(self):
        for j in range(4):
            for i in range(3):
                if self.board[self.coordtoindx(i+1,j)]==0:
                    self.board[self.coordtoindx(i+1,j)] = self.board[self.coordtoindx(i,j)]
                    self.board[self.coordtoindx(i,j)] = 0
                elif self.board[self.coordtoindx(i+1,j)] == self.board[self.coordtoindx(i,j)]:
                    self.board[self.coordtoindx(i+1,j)] = self.board[self.coordtoindx(i+1,j)] + self.board[self.coordtoindx(i,j)]
                    self.board[self.coordtoindx(i,j)] = 0
        for j in range(4):
            for i in range(3):
                if self.board[self.coordtoindx(i+1,j)]==0:
                    self.board[self.coordtoindx(i+1,j)] = self.board[self.coordtoindx(i,j)]
                    self.board[self.coordtoindx(i,j)] = 0

    def left(self):
        for j in range(4):
            for i in range(3):
                if self.board[self.coordtoindx(2-i,j)]==0:
                    self.board[self.coordtoindx(2-i,j)] = self.board[self.coordtoindx(3-i,j)]
                    self.board[self.coordtoindx(3-i,j)] = 0
                elif self.board[self.coordtoindx(2-i,j)] == self.board[self.coordtoindx(3-i,j)]:
                    self.board[self.coordtoindx(2-i,j)] = self.board[self.coordtoindx(2-i,j)] + self.board[self.coordtoindx(3-i,j)]
                    self.board[self.coordtoindx(3-i,j)] = 0
        for j in range(4):
            for i in range(3):
                if self.board[self.coordtoindx(2-i,j)]==0:
                    self.board[self.coordtoindx(2-i,j)] = self.board[self.coordtoindx(3-i,j)]
                    self.board[self.coordtoindx(3-i,j)] = 0
    
    def down(self):
        for i in range(4):
            for j in range(3):
                if self.board[self.coordtoindx(i,j+1)]==0:
                    self.board[self.coordtoindx(i,j+1)] = self.board[self.coordtoindx(i,j)]
                    self.board[self.coordtoindx(i,j)] = 0
                elif self.board[self.coordtoindx(i,j+1)] == self.board[self.coordtoindx(i,j)]:
                    self.board[self.coordtoindx(i,j+1)] = self.board[self.coordtoindx(i,j+1)] + self.board[self.coordtoindx(i,j)]
                    self.board[self.coordtoindx(i,j)] = 0
        for i in range(4):
            for j in range(3):
                if self.board[self.coordtoindx(i,j+1)]==0:
                    self.board[self.coordtoindx(i,j+1)] = self.board[self.coordtoindx(i,j)]
                    self.board[self.coordtoindx(i,j)] = 0
    
    def up(self):
        for i in range(4):
            for j in range(3):
                if self.board[self.coordtoindx(i,2-j)]==0:
                    self.board[self.coordtoindx(i,2-j)] = self.board[self.coordtoindx(i,3-j)]
                    self.board[self.coordtoindx(i,3-j)] = 0
                elif self.board[self.coordtoindx(i,2-j)] == self.board[self.coordtoindx(i,3-j)]:
                    self.board[self.coordtoindx(i,2-j)] = self.board[self.coordtoindx(i,2-j)] + self.board[self.coordtoindx(i,3-j)]
                    self.board[self.coordtoindx(i,3-j)] = 0
        for i in range(4):
            for j in range(3):
                if self.board[self.coordtoindx(i,2-j)]==0:
                    self.board[self.coordtoindx(i,2-j)] = self.board[self.coordtoindx(i,3-j)]
                    self.board[self.coordtoindx(i,3-j)] = 0





myGame = Game()
for i in range(10):
    myGame.addRandom()

myGame.printboard()

myGame.up()
myGame.printboard()
