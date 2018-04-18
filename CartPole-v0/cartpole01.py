import gym
import numpy as np

STEPS    = None
EPISODES = None
ENV      = None

def to_action(parameters, observations): # -> action
    return int(np.matmul(parameters, observations) >= 0)

def run_episode(parameters):
    observations = ENV.reset()
    total_reward = 0
    for _ in range(STEPS):
        parameters 
        observations, reward, done, info = ENV.step(
            to_action(parameters, observations))
        total_reward += reward
        if done: break
    return total_reward

def run_experiment(parameters):
    print("Experiment:",parameters,end="")
    avg_reward = 0
    for _ in range(EPISODES):
        avg_reward += run_episode(parameters)
    avg_reward /= EPISODES
    print("| Average Reward:",avg_reward)
    return avg_reward


def init(_STEPS, _EPISODES):
    global STEPS, EPISODES, ENV
    STEPS, EPISODES = _STEPS, _EPISODES
    ENV = gym.make("CartPole-v0")

def run(experiments):
    max_parameters = None
    max_reward     = 0
    for parameters in experiments:
        average_reward = run_experiment(parameters)
        if average_reward > max_reward:
            max_parameters = parameters
            max_reward     = average_reward    
    print("-----------------------------------------")
    print("Max Parameters :", max_parameters)
    print("Max Reward     :", max_reward)
    return max_parameters, max_reward