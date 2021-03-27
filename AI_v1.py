from game import *
from random import randint
import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
import math

active_game = Game2048(human=False)

device = 'cuda' if torch.cuda.is_available() else 'cpu'
print('Using {} device'.format(device))
'''
moves = ['w','a','s','d']
while not active_game.terminal:
    active_game.step(moves[randint(0,3)])
'''



class DQN(nn.Module):
    def __init__(self):
        super(DQN, self).__init__()
        self.linear_relu_stack = nn.Sequential(
            nn.Linear(4*4,16*16),
            nn.ReLU(),
            nn.Linear(16*16,16*6),
            nn.ReLU(),
            nn.Linear(16*6, 16),
            nn.ReLU(),
            nn.Linear(16,4)
        )

    def forward(self, x):
        logits = self.linear_relu_stack(x)
        return logits

'''
model = DQN().to(device)
print(model)
print(model(torch.Tensor(np.ones(16))))
'''


def train(episodes):
    episode = 0
    model = DQN().to(device)
    while episode<episodes:
        new_game = Game2048(human=False)
        state = [0 for i in range(16)]
        output = [0 for i in range(16)]
        while type(output) == list:
            state = int(math.log2(np.array(output)))
            


            output = new_game.step(action)





        episode+=1

    pass