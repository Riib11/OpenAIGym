import gym

episodes = 1
steps    = 200

env = gym.make("Breakout-v0")

for i_episode in range(episodes):
    observation = env.reset()
    for t in range(steps):
        # render
        env.render()
        # log
        print(observation)
        
        # random action
        action = env.action_space.sample()
        print(action)
        
        # update
        observation, reward, done, info = env.step(action)
        if done:
            print("Episode "+str(i_episode)+" finished after "+str(t)+" timesteps")
            break