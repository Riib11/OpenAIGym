import gym
import numpy as np

experiments = 10
steps       = 11

# init environment
env = gym.make("CartPole-v0")

# define how to combine parameters and observation to get an action
def get_action(parameters, observation):
    return int(np.matmul(parameters, observation) >= 0)

#
# Episode
# > a single run with a set of parameters
#
def run_episode(parameters, target):
    observation = env.reset()
    total_reward = 0

    for _ in range(steps):
        action = get_action(parameters, observation)
        observation, reward, done, info = env.step(action)
        # env.render()
        total_reward += reward
        if done or total_reward >= target:
            break
    
    # success?
    return total_reward >= target

# 
# Experiment
# > tests a set of parameters
#
def run_experiment(parameters, target):
    print("Experiment:",parameters)
    episode_count = 0
    while True:
        # run episode
        succ = run_episode(parameters, target)
        episode_count += 1
        if succ:
            break
    print("* episodes: ", episode_count)
    return episode_count

#
# Main
#
def main():
    inc = 0.01
    # parameters = np.random.rand(4) * 2 - 1
    parameters = [-0.3611937,   0.07714128, -0.81386741,  0.99992824]
    best_episodes = 1000000000000
    best_parameters = None
    target = steps

    for i_exp in range(experiments):
        # parameters = np.random.rand(4) * 2 - 1         # init parameters
        episodes = run_experiment(parameters, target)  # run experiment
        if episodes < best_episodes:                   # update bests
            best_episodes = episodes
            best_parameters = parameters
            parameters = mutate(parameters)

    print("----------------------------------------------------------")
    print("Best Parameters:", best_parameters)
    print("Best Episodes:", best_episodes)

# run
main()