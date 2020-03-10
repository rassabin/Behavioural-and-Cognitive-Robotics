import gym
import numpy as np
from operator import itemgetter
env = gym.make('CartPole-v0')

ninputs = env.observation_space.shape[0]
if (isinstance(env.action_space, gym.spaces.box.Box)):
 noutputs = env.action_space.shape[0]
else:
 noutputs = env.action_space.n
nhiddens=10
pvariance = 0.1 # variance of initial parameters
ppvariance = 0.02 # variance of perturbations
# initialize the training parameters randomly by using a gaussian distribution with average 0.0 and variance 0.1
# biases (thresholds) are initialized to 0.0
W1 = np.random.randn(nhiddens,ninputs) * pvariance # first layer
W2 = np.random.randn(noutputs, nhiddens) * pvariance # second layer
b1 = np.zeros(shape=(nhiddens, 1)) # bias first layer
b2 = np.zeros(shape=(noutputs, 1)) # bias second layer
def initialize_weights(n,ninputs,nhiddens,noutputs):
    par_dic=[]
    for i in range(n):
        par_dic.append( {"W1": np.random.randn(nhiddens,ninputs),
                    "W2": np.random.randn(noutputs, nhiddens),
                    "b1": np.zeros((nhiddens, 1)),
                    "b2": np.zeros((noutputs, 1))})
    
    return par_dic



def predict(observation,W1,W2,b1,b2):
    Z1 = np.dot(W1, observation) + b1
    A1 = np.tanh(Z1)
    Z2 = np.dot(W2, A1) + b2
    A2 = np.tanh(Z2)
    if (A2[0] < 0):
        action = 0
    else:
        action = 1
    return action

def add_noise(dic,n):
    for i in range(int(n/2)):
        dic[i]['W1']=dic[int(n/2)+i]['W1']+np.random.randn(nhiddens,ninputs)*ppvariance
        dic[i]['W2']=dic[int(n/2)+i]['W2']+np.random.randn(noutputs, nhiddens)*ppvariance
        dic[i]['b1']=dic[int(n/2)+i]['b1']+np.random.randn(nhiddens, 1)*ppvariance
        dic[i]['b2']=dic[int(n/2)+i]['b2']+np.random.randn(noutputs, 1)*ppvariance
    return dic



reward1=0
popul = 10
par_dic = initialize_weights(popul,ninputs,nhiddens,noutputs)
t1 = 0
flag = 1
while(flag): 
    for i in range(popul):
        observation = env.reset()
        reward1 = 0
        for t in range(200):
            observation.resize(ninputs, 1)
            W1 = par_dic[i]['W1']
            W = par_dic[i]['W2']
            b1 = par_dic[i]['b1']
            b2 = par_dic[i]['b2']
            action = predict(observation,W1,W2,b1,b2)
            observation, reward, done, info = env.step(action)
            reward1=reward1+reward
            if done == True:
                    t1 = t
                    par_dic[i]['reward']=reward1
                    break      
    par_dic = sorted(par_dic,key=itemgetter('reward'))
    print(par_dic[len(par_dic)-1]['reward']) 
    par_dic = add_noise(par_dic,popul)
    if par_dic[len(par_dic)-1]['reward']>199.0:
        print('we are done now!!!')
        flag = 0
        break















 
