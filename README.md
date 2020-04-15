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
Average Generalization of the 3 fir files equal to: -136.20 +-51.85.
Also the test for each robot was performed the results you can find in video files in "data" folder. Observation also show that pend_S12 do not reach any result in training. 
All trained files you can find in "result" folder.

## Task 4


## Task 5
For building new robot in Gym/Bullet environment was created next structure of the project:
```
balance-bot/
  README.md
  setup.py
  balance_bot/
    __init__.py
    envs/
      __init__.py
      balancebot_env.py
```

All files was copied from pdf guideline. Also from original directories was copyied the xml with physical structure of the robot. 
After it the balance-bot module was building by pip. The zip archive contains of balance_bot project you can find in 'data' folder of repository.
In order to proving of succefully building of the module was used the script:
```python
import balance_bot
import gym
from gym import wrappers

env = gym.make('balancebot-v0')
env.reset()

for _ in range(1000):
    action = env.action_space.sample()
    observation, reward, done, info = env.step(action)
    print(observation)
    if done:
        break
env.close()
```

And on the output we get:
```
[-0.13050552 -0.16286352 -0.45825616]
[-0.1292571   0.12484095  0.49442795]
[-0.12526864  0.39884606  1.4044598 ]
[-0.11884049  0.64281577  2.220279  ]
[-0.11520612  0.36343586  1.3967034 ]
[-0.11225248  0.2953644   1.2380347 ]
[-0.10678178  0.54706967  2.0823307 ]
[-0.09915692  0.76248634  2.814029  ]
[-0.08904253  1.0114393   3.6522746 ]
[-0.08210314  0.693939    2.723149  ]
[-0.07545424  0.66489017  2.7005112 ]
[-0.06939755  0.60566854  2.5876074 ]
[-0.06490126  0.4496286   2.1088486 ]
[-0.06027702  0.46242404  2.1555905 ]
[-0.0544146  0.5862422  2.5533378]
[-0.04807988  0.63347214  2.7148204 ]
[-0.04170892  0.6370956   2.7440743 ]
[-0.03407753  0.76313937  3.1603687 ]
[-0.02696915  0.7108381   3.0231023 ]
[-0.02164867  0.53204757  2.4968917 ]
[-0.01837594  0.32727322  1.8942107 ]
[-0.01270791  0.5668034   2.684022  ]
[-0.00454975  0.8158156   3.428265  ]
[0.0043274  0.88771516 3.6281147 ]
[0.010627   0.62996006 2.8037689 ]
[0.01805607 0.74290705 3.1436214 ]
[0.0227329  0.46768272 2.2758014 ]
[0.0249235  0.21906018 1.494903  ]
[0.02964626 0.47227564 2.2856953 ]
[0.03411409 0.44678357 2.2099514 ]
[0.04104902 0.6934929  2.9898458 ]
[0.04780489 0.6755868  2.9478192 ]
[0.05788091 1.0076019  3.901283  ]
[0.06819861 1.0317707  3.9254787 ]
[0.07939456 1.1195952  4.154828  ]
[0.09302978 1.3635216  4.8788657 ]
[0.10469841 1.1668627  4.232939  ]
[0.11745783 1.275942   4.549789  ]
[0.13335252 1.5894684  5.3763666 ]
[0.15022363 1.6871107  5.5915275 ]
[0.1679616 1.7737976 5.785486 ]
[0.18865761 2.069601   6.644297  ]
[0.2109134 2.2255795 7.077738 ]
[0.2352499 2.4336503 7.446259 ]
[0.26025572 2.5005815  7.534233  ]
[0.28277504 2.2519329  6.64709   ]
[0.30718228 2.4407222  7.1444073 ]
[0.3344455 2.726322  7.6550612]
[0.35934886 2.4903364  6.736655  ]
[0.38417882 2.4829953  6.5578322 ]
[0.40787283 2.3694026  6.018731  ]
[0.4352364 2.7363572 7.004975 ]
[0.46591935 3.0682948  7.5323486 ]
[0.49886838 3.2949014  8.008335  ]
[0.5295865 3.0718112 7.0442605]
[0.5582443 2.865783  6.123766 ]
[0.591168  3.2923648 6.92126  ]
[0.6244486 3.3280613 6.7149134]
[0.65974814 3.5299535  6.9904785 ]
[0.69649667 3.6748571  7.0757966 ]
[0.73288906 3.6392348  6.540643  ]
[0.7700157 3.7126706 6.326185 ]
[0.80793387 3.7918146  5.793609  ]
[0.8463032 3.836934  5.4059854]
[0.88476634 3.8463137  4.410074  ]
[0.9243855 3.9619122 4.5812507]
[0.96584344 4.145795   4.5389023 ]
[1.0080924 4.2248974 3.7169676]
[1.0535026 4.541016  4.429742 ]
[1.0999337 4.643122  3.4872992]
[1.1480529 4.8119164 3.373357 ]
[1.1977339 4.9680915 2.8852825]
[1.2496866 5.195278  2.00539  ]
[1.3039818 5.429514  2.7935822]
[1.3617475 5.7765656 3.460238 ]
```
## Task 6


