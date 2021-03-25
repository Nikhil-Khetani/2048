
class Game():
    def __init__(self):
        self.boardx = 4
        self.boardy = 4
        self.board = [0 for i in range(self.boardx*self.boardy)]
        pass

    def printboard(self):
        for i in range(self.boardy):
            print("{}      {}      {}      {}".format(self.board[4*i-4],self.board[4*i-3],self.board[4*i-2], self.board[4*i-1]))
            print("")

    def addRandom(self):
        pass
    def coordtoindx(self,x,y):
        return 4*y+x
    
    def indxtocoord(self, index):
        x = index%4
        y = (index-x)/4
        return x, y

myGame = Game()
myGame.printboard()
