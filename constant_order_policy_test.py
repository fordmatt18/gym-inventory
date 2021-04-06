r = 1-(1/3)**(1/2) #value for constant order policy

# let lambda = p = h = L = 1
# then the optimal constant order policy has r_inf = 1 - srt(1/3) (approx .423)
# and the optimal constant order policy has a long run average cost of
#   C(pi_{r_inf}) = sqrt(3) - 1 (approx .732)
 
import gym 
from inventory_env import Inventory 
import numpy as np


env = Inventory(length = 10000) # create  the  inventory  network  environment  with default parameters
n_episodes = 100 # number  of  episodes  to  run
avg_reward = np.zeros(n_episodes)
for i in range(n_episodes):
    
    done = False
    env.reset()
    avg_r = 0
    
    while not done:
        action = np.array([r])
        obs, reward, done, info = env.step(action)
        avg_r = reward + avg_r
    
    avg_reward[i] = avg_r
    print(avg_r)
print(np.mean(avg_reward), '+/-', 1.96*np.std(avg_reward)/np.sqrt(n_episodes))