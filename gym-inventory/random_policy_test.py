import gym 
from inventory_env import Inventory 
import numpy as np

env = Inventory() # create  the  inventory  network  environment  with default parameters
n_episodes = 100 # number  of  episodes  to  run
avg_reward = np.zeros(n_episodes)
for i in range(n_episodes):
    
    done = False
    env.reset()
    avg_r = 0
    
    while not done:
        action = env.action_space.sample()
        obs, reward, done, info = env.step(action)
        avg_r = reward + avg_r
    
    avg_reward[i] = avg_r
    print(avg_r)
print(np.mean(avg_reward), '+/-', 1.96*np.std(avg_reward)/np.sqrt(n_episodes))
    