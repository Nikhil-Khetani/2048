# 2048
A version of the popular game "2048" that can be played in the command line and versions of a reinforcement learning algorithm with a DQN network to play the game.

#### Version 1, 2, 3
The DQN algorithm consistently gets above 2048 after just a few episodes of training. However, following this, performance does not seem to improve consistently. Note that versions 1 & 2 were not successful in batching data properly and therefore version 3 produced the best results.

#### Version 4
As opposed to methods used in previous versions, here a pure Monte Carlo game search (tree) is used to determine which move to take, dynamically changing the length of the rollout depending on the board state. This performed worse than version 3 given the time limits available.

## Instructions
```
python game.py
```
## Prerequisites
This project only requires standard Python libraries to play the game.
To train the reinforcement learning agent, PyTorch and NumPy are required:
```
pip install torch
pip install numpy
```
## Built with
+ Visual Studio Code

## Authors
+ Nikhil Khetani

## License
This project is licensed under the GNU General Public License v3.0 - see the [LICENSE.md](/LICENSE) file for details.
