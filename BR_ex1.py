import gym
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('env',type=str, help='Using envirement. Possible values: CartPole-v0, CartPole-v1, Acrobot-v1, Pendulum-v0, MountainCar-v0')
args = parser.parse_args()
if args.env not in ['CartPole-v0', 'CartPole-v1', 'Acrobot-v1', 'Pendulum-v0', 'MountainCar-v0']:
    print('Wrong env name')
else:
    print('Success')
    env = gym.make(args.env)
    print('Action space is',env.action_space)
    print('Observation space is',env.observation_space)
    print('The max value of observation space is ',env.observation_space.high,'and the lowest one',print(env.observation_space.low))
    env.reset()
    for i in range(200):
        observation, reward, done, info = env.step(env.action_space.sample())
        print('Observation for ',i,'step is',observation)
    env.close()