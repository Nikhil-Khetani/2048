from game import *
from random import randint
import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
import math
import random

from collections import namedtuple


image_size=84
batch_size=32
lr=1e-6
gamma=0.99
initial_epsilon=0.1
final_epsilon=1e-4
num_iters=2000000
#replay_memory_size=50000

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
Transition = namedtuple('Transition',
                        ('state', 'action', 'next_state', 'reward'))


class ReplayMemory(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.memory = []
        self.position = 0

    def push(self, *args):
        """Saves a transition."""
        if len(self.memory) < self.capacity:
            self.memory.append(None)
        self.memory[self.position] = Transition(*args)
        self.position = (self.position + 1) % self.capacity

    def sample(self, batch_size):
        return random.sample(self.memory, batch_size)

    def __len__(self):
        return len(self.memory)

def calcReward(state):
    empties = 0
    total = 0
    highest = 0 
    for i in state:
        if i == 0:
            empties+=1
        else:
            total+=i
        highest = max(highest,i)
    return (total+highest)/(empties+highest)




def train(episodes):
    episode = 0
    moves = ['w','a','s','d']
    mem = ReplayMemory(10000)
    model = DQN().to(device)
    episode = 0
    while episode<episodes:
        new_game = Game2048(human=False)
        optimizer = torch.optim.Adam(model.parameters(), lr=1e-6)
        criterion = torch.nn.MSELoss()
        next_state = torch.Tensor(np.array([0 for i in range(16)]))
        output = [0 for i in range(16)]
        while type(output) == list:
            state = next_state
            pred = model(state)
            action = moves[torch.argmax(pred).item()]
            epsilon = final_epsilon+((episodes-episode)*(initial_epsilon-final_epsilon)/episodes)
            take_random_action = random.random()<=epsilon
            if take_random_action:
                print('random')
                action = moves[random.randint(0,3)]
            #else:
                #action=torch.argmax(pred)


            output = new_game.step(action)
            next_state = torch.Tensor(np.array([math.log2(i) if i!=0 else i for i in output]))
            #next_state = math.log2(np.array(output))

            if new_game.getTerminal():
                reward = -1
            else:
                reward = calcReward(next_state)

            mem.push(state,action,next_state,reward) # might need endgame in list

            if len(mem)>64:
                batch = mem.sample(batch_size)
                print(batch)
                state_batch, action_batch, reward_batch, next_state_batch = zip(*batch)
            
                current_prediction_batch = model(state_batch)
                next_prediction_batch = model(next_state_batch)
                y_batch = torch.cat(tuple(reward + gamma * torch.max(prediction) for reward, prediction in zip(reward_batch, next_prediction_batch)))

                q_value = torch.sum(current_prediction_batch * action_batch, dim=1)
                optimizer.zero_grad()
                # y_batch = y_batch.detach()
                loss = criterion(q_value, y_batch)
                loss.backward()
                optimizer.step()

                print("Iteration: {}/{}, Action: {}, Loss: {}, Epsilon {}, Reward: {}, Q-value: {}".format(
                episode + 1,
                num_iters,
                action,
                loss,
                epsilon, reward, torch.max(pred)))

            if new_game.getTerminal():
                break

        episode+=1

    pass

train(100)