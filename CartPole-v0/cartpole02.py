import gym
import numpy as np

def init(STEPS=200, EPISODES=100, TRIALS=100, INC=0.01):
    global _STEPS, _EPISODES, _ENV, _TRIALS, _INC
    _STEPS, _EPISODES, _TRIALS, _INC = STEPS, EPISODES, TRIALS, INC
    _ENV = gym.make("CartPole-v0")

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
    print("Experiment:",parameters,end="")
    avg_reward = 0
    for _ in range(_EPISODES):
        avg_reward += run_episode(parameters)
    avg_reward /= _EPISODES
    print(" | Average Reward:",avg_reward)
    return avg_reward

def run(parameters=None):
    parameters = parameters or np.random.rand(4) * 2 - 1
    reward     = run_experiment(parameters)
    
    for trial in range(_TRIALS):
        for ind in range(len(parameters)):
            for d in [-_INC,_INC]:
                # step
                n = parameters[ind] + d
                n = max(n,-1)
                n = min(n,1)
                parameters[ind] = n
                parameters[ind] += d 
                new_reward = run_experiment(parameters)
                if new_reward < reward:
                    parameters[ind] -= d # undo step
                else:
                    reward = new_reward
                print("| ["+str(trial)+"] Reward: "+str(reward))

    print("-----------------------------------------")
    print("Max Parameters :", parameters)
    print("Max Reward     :", reward)
    return parameters, reward