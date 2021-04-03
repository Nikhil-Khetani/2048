# 2048
A version of the popular game "2048" that can be played in the command line and versions of a reinforcement learning algorithm with a DQN network to play the game.

#### Update Version 2
The algorithm consistently gets above 2048 after just a few episodes of training. However, following this, performance does not seem to improve consistently. In Version 3 I hope to update the inputs to the model by adding more features dependent on when a tile matches an adjacent one so as to better input the data to the network.

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
