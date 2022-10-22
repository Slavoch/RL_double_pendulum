# Reinforcement learning for stabilising double inverted pendulum
This is a final project of Reinforcement learning course at skoltech which is devoted for stabilising double inverted pendulum


# 

Algorithms which was used
- Proximal policy optimization (PPO)
- Model predictive control (MPC)
- Deep double Q-network (DDQN)

## Folders and Files Description

### Folders and files

|Folder name       |                     Description                                    |
|------------------|--------------------------------------------------------------------|
|`1_pole_inverted_pendulum`             |  Source code for simple case of inverted pendulum                                           |
|`DDQN`            | Results of training deep double Q-network for stabilising double inverted pendulum                              |
|`MPC`          | Model predictive control using Casadi optimization                 |
|`MPC`          |  Results of training Proximal policy optimization for stabilising double inverted pendulum                 |


### Files

|File name            |                     Description                                    |
|---------------------|--------------------------------------------------------------------|
|`Dynamics.py`            | Double inverted pendulum dynamics which was written on Casadi    |
|`Environment.py`          | Containing the SAc agent class                                     |
|`networks.py`        | Networks in used by agents (Actor, Critic and Value networks)      |
|`utils.py`           | General utility functions                                          |
|`buffer.py`          | A replay buffer class, used for offline training                   |


You can see below the learning curves along with gifs of agents  play the Inverted Double Pendulum and Inverted Pendulum Swing environment.
## Proximal policy optimization 
Episode rewards curves:

Random initial state (90 +- 3 degrees)
<p align="center">
<img src="https://user-images.githubusercontent.com/53058704/197342315-3c3afa99-9ba3-4a4e-b0fa-f3119e7fe339.png" width="500">
</p>


Fixed initial state (90 degrees)
<p align="center">
<img  src="https://user-images.githubusercontent.com/53058704/197342642-01feb722-0eac-4e39-8b77-87731752b208.png" width="500">
</p>



Agent after 100k timesteps of training
![PPO_100K](https://user-images.githubusercontent.com/53058704/197342394-5273b20d-a462-4ffc-bd20-7fb08159e4ed.gif)


Agent after 500k timesteps of training
![PPO_500K](https://user-images.githubusercontent.com/53058704/197342398-55ca8314-a958-4e78-b3b6-6c6901a39e16.gif)


Agent after 1000k timesteps of training
![PPO_1000K](https://user-images.githubusercontent.com/53058704/197342402-f543e5f5-07e7-4573-b78d-378036598564.gif)




## Model predictive control



## How to use
