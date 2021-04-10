from copy import copy
class Game_2048():
    def __init__(self, board=None, turn='r', depth=0):
        super().__init__()
        if board==None:
            self.board =self.board = [0 for i in range(4*4)]
        else:
            self.board = board
        self.turn = turn
        self.depth = depth
        self.legal_moves = []
        self.children = []
        self.explored = False

        self.findLegalMoves()
        if len(self.legal_moves)==0:
            self.terminal = True
        else:
            self.terminal = False

    def explore(self, depth = None):
        if depth != None:
            self.depth = depth
        if self.terminal:
            self.survive_prob = 0
            return 0
        elif self.depth==0:
            self.survive_prob = 1
            return 1
        if not self.explored:
            if self.turn == 'p':
                opposite_turn = 'r'
            else:
                opposite_turn = 'p'

            for move in self.legal_moves:
                if self.turn == 'p':
                    self.children.append(Game_2048(board = move(copy(self.board)),turn = opposite_turn,depth = self.depth-1))
                else:
                    self.children.append(Game_2048(board = self.putTwo(copy(self.board), move), turn = opposite_turn, depth = self.depth-1))
            self.explored = True
        
        self.children_survive_prob = []
        for child in self.children:
            self.children_survive_prob.append(child.explore())
        if self.turn == 'p':
            self.survive_prob = max(self.children_survive_prob)
            return self.survive_prob
        else:
            self.survive_prob = sum([child_survive_prob/len(self.children) for child_survive_prob in self.children_survive_prob])
            return self.survive_prob
        
    def printChildrenSurviveProb(self):
        print(self.legal_moves)
        print('Len self.children {}'.format(len(self.children)))
        for i in range(len(self.legal_moves)):
            print('{} : Survival = {}'.format(self.legal_moves[i], self.children[i].survive_prob))



    def findLegalMoves(self):
        if self.turn == 'r':
            for i in range(len(self.board)):
                if self.board[i] == 0:
                    self.legal_moves.append(i)
        else:
            if self.board != self.up(copy(self.board)):
                self.legal_moves.append(self.up)
            if self.board != self.left(copy(self.board)):
                self.legal_moves.append(self.left)
            if self.board != self.down(copy(self.board)):
                self.legal_moves.append(self.down)
            if self.board != self.right(copy(self.board)):
                self.legal_moves.append(self.right)
        pass

    def coordtoindx(self,x,y):
        return 4*y+x
    
    def indxtocoord(self, index):
        x = index%4
        y = int((index-x)/4)
        return x, y


    def right(self, checkboard):
        for j in range(4):
            for i in range(3):
                if checkboard[self.coordtoindx(i+1,j)]==0:
                    checkboard[self.coordtoindx(i+1,j)] = checkboard[self.coordtoindx(i,j)]
                    checkboard[self.coordtoindx(i,j)] = 0
                elif checkboard[self.coordtoindx(i+1,j)] == checkboard[self.coordtoindx(i,j)]:
                    checkboard[self.coordtoindx(i+1,j)] = checkboard[self.coordtoindx(i+1,j)] + checkboard[self.coordtoindx(i,j)]
                    checkboard[self.coordtoindx(i,j)] = 0
        for j in range(4):
            for i in range(3):
                if checkboard[self.coordtoindx(i+1,j)]==0:
                    checkboard[self.coordtoindx(i+1,j)] = checkboard[self.coordtoindx(i,j)]
                    checkboard[self.coordtoindx(i,j)] = 0
        return checkboard

    def left(self, checkboard):
        for j in range(4):
            for i in range(3):
                if checkboard[self.coordtoindx(2-i,j)]==0:
                    checkboard[self.coordtoindx(2-i,j)] = checkboard[self.coordtoindx(3-i,j)]
                    checkboard[self.coordtoindx(3-i,j)] = 0
                elif checkboard[self.coordtoindx(2-i,j)] == checkboard[self.coordtoindx(3-i,j)]:
                    checkboard[self.coordtoindx(2-i,j)] = checkboard[self.coordtoindx(2-i,j)] + checkboard[self.coordtoindx(3-i,j)]
                    checkboard[self.coordtoindx(3-i,j)] = 0
        for j in range(4):
            for i in range(3):
                if checkboard[self.coordtoindx(2-i,j)]==0:
                    checkboard[self.coordtoindx(2-i,j)] = checkboard[self.coordtoindx(3-i,j)]
                    checkboard[self.coordtoindx(3-i,j)] = 0
        return checkboard
    
    def down(self, checkboard):
        for i in range(4):
            for j in range(3):
                if checkboard[self.coordtoindx(i,j+1)]==0:
                    checkboard[self.coordtoindx(i,j+1)] = checkboard[self.coordtoindx(i,j)]
                    checkboard[self.coordtoindx(i,j)] = 0
                elif checkboard[self.coordtoindx(i,j+1)] == checkboard[self.coordtoindx(i,j)]:
                    checkboard[self.coordtoindx(i,j+1)] = checkboard[self.coordtoindx(i,j+1)] + checkboard[self.coordtoindx(i,j)]
                    checkboard[self.coordtoindx(i,j)] = 0
        for i in range(4):
            for j in range(3):
                if checkboard[self.coordtoindx(i,j+1)]==0:
                    checkboard[self.coordtoindx(i,j+1)] = checkboard[self.coordtoindx(i,j)]
                    checkboard[self.coordtoindx(i,j)] = 0
        return checkboard
    
    def up(self,checkboard):
        for i in range(4):
            for j in range(3):
                if checkboard[self.coordtoindx(i,2-j)]==0:
                    checkboard[self.coordtoindx(i,2-j)] = checkboard[self.coordtoindx(i,3-j)]
                    checkboard[self.coordtoindx(i,3-j)] = 0
                elif checkboard[self.coordtoindx(i,2-j)] == checkboard[self.coordtoindx(i,3-j)]:
                    checkboard[self.coordtoindx(i,2-j)] = checkboard[self.coordtoindx(i,2-j)] + checkboard[self.coordtoindx(i,3-j)]
                    checkboard[self.coordtoindx(i,3-j)] = 0
        for i in range(4):
            for j in range(3):
                if checkboard[self.coordtoindx(i,2-j)]==0:
                    checkboard[self.coordtoindx(i,2-j)] = checkboard[self.coordtoindx(i,3-j)]
                    checkboard[self.coordtoindx(i,3-j)] = 0
        return checkboard
    
    def putTwo(self,checkboard,index):
        checkboard[index] = 2
        return checkboard

    def printboard(self):
        print("################################################")
        print("")
        for j in range(4):
            print(" {:5}      {:5}      {:5}      {:5}".format(self.board[4*j],self.board[4*j+1],self.board[4*j+2], self.board[4*j+3]))
            print("")
        print("################################################")
        return


if __name__ == '__main__':
    
    myGame = Game_2048(depth = 3)
    while myGame.terminal == False:
        myGame.printboard()
        num_to_explore = max(11-myGame.board.count(0),5)
        print('survival prob = {}'.format(myGame.explore(num_to_explore)))
        myGame.printChildrenSurviveProb()
        myGame = myGame.children[max(zip(myGame.children_survive_prob, range(len(myGame.children_survive_prob))))[1]]
        

