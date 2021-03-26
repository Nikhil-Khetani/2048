from random import randint
from copy import copy
class Game():
    def __init__(self, human=True):
        self.boardx = 4
        self.boardy = 4
        self.board = [0 for i in range(self.boardx*self.boardy)]
        self.turn = 0
        self.empties = []
        self.human = human
        self.functions =    {
                            'w': self.up,
                            'a': self.left,
                            's': self.down,
                            'd': self.right,
                            }
        self.step(input())
        pass

    def printboard(self):
        
        print("########################")
        print("")
        for j in range(self.boardy):
            print(" {}      {}      {}      {}".format(self.board[4*j],self.board[4*j+1],self.board[4*j+2], self.board[4*j+3]))
            print("")
        print("########################")
        print("Turn: {}".format(self.turn))
        return

    def addRandom(self):
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

    
    def step(self, action):
        put_random=True
        self.turn+=1
        self.functions[action]()
        
        if len(self.getEmpties())==0:
            if self.checkEnd():
                self.endGame()
                return
            else:
                put_random = False

        if put_random:
            self.addRandom()

        self.printboard()
        if self.human:
            new_action = input()
            if new_action == 'q':
                self.endGame()
                return
            self.step(new_action)
        
    def checkEnd(self):
        original = copy(self.board)
        self.up()
        if original==self.board:
            self.right()
            if original==self.board:
                self.down()
                if original==self.board:
                    self.left()
                    if original==self.board:
                        return True
        self.board = copy(original)    
        return False

    def endGame(self):
        print("########################")
        print("########GAME OVER#######")
        self.printboard
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





myGame = Game(human=True)

myGame.printboard()

