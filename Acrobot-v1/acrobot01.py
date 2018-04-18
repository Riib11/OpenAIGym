import gym
import numpy as np
import utils

def init(STEPS=200, EPISODES=100, TRIALS=100, INC=0.01):
    global _STEPS, _EPISODES, _ENV, _TRIALS, _INC
    _STEPS, _EPISODES, _TRIALS, _INC = STEPS, EPISODES, TRIALS, INC
    _ENV = gym.make("Acrobot-v1")

def to_action(parameters, observations): # -> action
    return int(np.matmul(parameters, observations) >= 0)

def run_episode(parameters):
    observations = _ENV.reset()
    total_reward = 0
    for _ in range(_STEPS):
        parameters 
        observations, reward, done, info = _ENV.step(
            to_action(parameters, observations))
        total_reward += reward
        if done: break
    return total_reward

def run_experiment(parameters):
    # print("Experiment:",parameters,end="")
    avg_reward = 0
    for _ in range(_EPISODES):
        avg_reward += run_episode(parameters)
    avg_reward /= _EPISODES
    # print(" | Average Reward:",avg_reward)
    return avg_reward

def int_to_binarr(x,shape):
    arr = []
    while x > 0:
        if x % 2 == 0:
            arr.append(0)
        else:
            arr.append(1)
        x = int(x/2)
    while len(arr) < shape:
        arr.append(0)
    return arr

def run(parameters):
    reward      = run_experiment(parameters)
    directions  = utils.all_directions(6,_INC,-_INC)
    pre_reward  = None
    
    for trial in range(_TRIALS):
        max_reward = reward
        max_params = parameters
        # try stepping in all directions
        for i in range(len(directions)):
            new_params = parameters.copy() + directions[i] # step
            new_reward = run_experiment(new_params)
            print(trial, new_reward, new_params)
            if new_reward > max_reward:
                max_reward = new_reward
                max_params = new_params
        # update parameters
        parameters = max_params
        reward     = max_reward
        print("-----------------------------------------")
        print("Max Parameters :", parameters)
        print("Max Reward     :", reward)
        print("-----------------------------------------")
        

    print("-----------------------------------------")
    print("Total Max Parameters :", parameters)
    print("Total Max Reward     :", reward)
    return parameters, reward