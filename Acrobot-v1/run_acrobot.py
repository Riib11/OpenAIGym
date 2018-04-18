import gym
import numpy as np
episodes = 1
steps    = 1000
env      = gym.make("Acrobot-v1") 

parameters = [-0.7, -0.09675654, 0.48592605000000005, -0.39999999999999997, -0.29418346999999995, 0.7952805199999999]
def to_action(observations): # -> action
    return int(np.matmul( parameters, observations) >= 0)

for i_episode in range(episodes):
    observations = env.reset()
    t, done = 0, False
    total_reward = 0
    while not done:
        env.render()                     # render
        # print(observations)              # log
        action = to_action(observations) # action 
        # update
        observations, reward, done, info = env.step(action) 
        t += 1
        total_reward += reward

    print("Episode "+str(i_episode)+" finished after "+str(t)+" timesteps")
    print("Total Reward:", total_reward)