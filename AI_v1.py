from game import *
from random import randint
import torch
import torch.nn as nn
import torch.nn.functional as F

active_game = Game2048(human=False)

device = 'cuda' if torch.cuda.is_available() else 'cpu'
print('Using {} device'.format(device))

moves = ['w','a','s','d']
while not active_game.terminal:
    active_game.step(moves[randint(0,3)])




class DQN(nn.Module):
    def __init__(self):
        super(DQN, self).__init__()
        self.flatten = nn.Flatten()
        self.linear_relu_stack = nn.Sequential(
            nn.Linear(4*4,16*16),
            nn.ReLU(),
            nn.Linear(16*16,16*6),
            nn.ReLU(),
            nn.Linear(16*6, 16),
            nn.ReLU(),
            nn.Linear(16,4)
        )
        self.softmax = nn.Softmax()

    def forward(self, x):
        x = self.flatten(x)
        x = self.linear_relu_stack(x)
        logits = self.softmax(x)
        return logits

model = DQN().to(device)
print(model)
def train(episodes):
    pass