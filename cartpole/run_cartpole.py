import gym
import numpy as np
episodes = 1
steps    = 1000
env      = gym.make("CartPole-v0") 

parameters = [-0.34920916,  0.83416068,  0.27887405,  0.70798517]
# parameters = [ 0.26350572,  1.10846221,  1.5,         1.5       ]
def to_action(observations): # -> action
    return int(np.matmul( parameters, observations) >= 0)

for i_episode in range(episodes):
    observations = env.reset()
    t, done = 0, False
    while not done:
        env.render()                                # render
        # print(observations)                         # log
        action = to_action(observations)            # action 
        observations, _, done, _ = env.step(action) # update
        t += 1

    print("Episode "+str(i_episode)+" finished after "+str(t)+" timesteps")
