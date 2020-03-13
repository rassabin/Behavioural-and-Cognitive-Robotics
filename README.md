# Behavioural-and-Cognitive-Robotics

## Task 1
The file BR_ex1.py requires the input envirement name such as 'CartPole-v0', 'CartPole-v1', 'Acrobot-v1', 'Pendulum-v0', 'MountainCar-v0'.
On the output you get the values of envirement variable:
env.action_space;
env.observation_space;
env.observation_space.high and env.observation_space.low;
Also script made the observation for the 200 steps and print it for each step.

## Task 2
The file BR_ex2.py contain neural network with 2 layers and 10 hidden neurons by default. This NN train to solve the CartPole-v0
problem in order to balance the pendulum in up position during the 200 steps. For solving this task used the evolution approach 
presented in guide file. By default population number of NN set to 10.The script output the best reward value from population 
after set of experimant (which is equal to number of population).
The problem is considered solved when any neural network from the population once holds the pendulum for 200 steps.

Chosen parameters allow us NN solve the each time. With decreaing number of hidden neurons the NN less and less 
solve task. Similar result with increasing the perturbance value, because it's harder to find the local optima with big step.

## Task 3
In order to train th NN was performed 3 expriments with different seed parameters: 10, 11, 12.
The train process across generation you see on the figure 
![Image of Yaktocat](https://github.com/rassabin/Behavioural-and-Cognitive-Robotics/blob/master/data/figure_1.png)
As you can see the model with seed equal to 12 do not train at all and best train result on model with seed = 10.
Also the test for each robot was performed the results you can find in video files in data folder. Observation also show that pend_S12 do not reach any result in training. 
