# Behavioural-and-Cognitive-Robotics
The file BR_ex1.py requires the input envirement name such as 'CartPole-v0', 'CartPole-v1', 'Acrobot-v1', 'Pendulum-v0', 'MountainCar-v0'.
On the output you get the values of envirement variable:
env.action_space;
env.observation_space;
env.observation_space.high and env.observation_space.low;
Also script made the observation for the 200 steps and print it for each step.

The file BR_ex2.py contain neural network with 2 layers and 10 hidden neurons by default. This NN train to solve the CartPole-v0
problem in order to balance the pendulum in up position during the 200 steps. For solving this task used the evolution approach 
presented in guide file. By default population number of NN set to 10.The script output the best reward value from population 
after set of experimant (which is equal to number of population).
The problem is considered solved when any neural network from the population once holds the pendulum for 200 steps.

Chosen parameters allow us NN solve the each time. With decreaing number of hidden neurons the NN less and less 
solve task. Similar result with increasing the perturbance value, because it's harder to find the local optima with big step.


