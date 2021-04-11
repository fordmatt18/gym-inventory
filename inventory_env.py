import gym
import numpy as np
import sys

class Inventory(gym.Env):

    def __init__(self, start_inv = 1, alpha = 1, h = 1, p = 1, L = 1, length = 10000): # note I just chose some default values
        self.start_inv = start_inv # starting inventory
        self.alpha = alpha  # parameter of exponenetial demand, 1/alpha is mean demand
        self.h = h  # holding cost
        self.p = p # lost sales penalty
        self.L = L # lead time
        self.length = length # how many periods to run simulation
        self.steps = 0 # keeps track of how many steps have been done in this episode
        self.state = np.zeros(self.L + 1) # first entry is current inventory, remaining entries are outstanding orders
        self.state[0] = self.start_inv # setting starting inventory
        self.action_space = gym.spaces.Box(low=0.0, high=np.inf, shape=(1,))
        self.observation_space = gym.spaces.Box(low=0.0, high=np.inf, shape=(self.L + 1,))
        self.seed()
        metadata = {'render.modes': ['ansi']}

    def seed(self, seed=None):
        self.np_random, seed = gym.utils.seeding.np_random(seed)
        return [seed]

    def step(self, action): # note action must be of an np array
        assert self.action_space.contains(action)
        
        #update on hand inventory
        on_hand = self.state[0] + self.state[1]
        
        #simulate demand
        demand = self.np_random.exponential(self.alpha)
        
        #post demand inventory
        on_hand_post = max(on_hand - demand, 0)
        
        #incur costs
        lost_sales = -min(on_hand - demand, 0)
        reward = -(self.h * on_hand_post  + self.p * lost_sales) / self.length
        
        #update pipeline vector
        next_state = np.zeros(self.L + 1)
        next_state[1:-1], next_state[-1] = self.state[2:], action
        next_state[0] = on_hand_post
        self.state = next_state
        self.steps = self.steps + 1
        
        done = (self.steps >= self.length)
        return self.state, reward, done, {}

    def render(self, mode='ansi'):
        outfile = sys.stdout if mode == 'ansi' else super(Inventory, self).render(mode=mode)
        outfile.write(np.array2string(self.state))

    def reset(self):
        self.steps = 0 # keeps track of how many steps have been done in this episode
        self.state = np.zeros(self.L + 1) # first entry is current inventory, remaining entries are outstanding orders
        self.state[0] = self.start_inv # setting starting inventory
        return self.state

















#import gym
#import numpy as np
#import sys

#class Inventory(gym.Env):

#    def __init__(self, start_inv = 1, alpha = 1, h = 1, p = 1, L = 1, length = 10000): # note I just chose some default values
#        self.start_inv = start_inv # starting inventory
#        self.alpha = alpha  # parameter of exponenetial demand, 1/alpha is mean demand
#        self.h = h  # holding cost
#        self.p = p # lost sales penalty
#        self.L = L # lead time
#        self.length = length # how many periods to run simulation
#        self.steps = 0 # keeps track of how many steps have been done in this episode
#        self.state = np.zeros(self.L + 1) # first entry is current inventory, remaining entries are outstanding orders
#        self.state[0] = self.start_inv # setting starting inventory
#        self.action_space = gym.spaces.Box(low=0.0, high=np.inf, shape=(1,))
#        self.observation_space = gym.spaces.Box(low=0.0, high=np.inf, shape=(self.L + 1,))
#        self.seed()
#        metadata = {'render.modes': ['ansi']}

#    def seed(self, seed=None):
#        self.np_random, seed = gym.utils.seeding.np_random(seed)
#        return [seed]

#    def step(self, action): # note action must be of an np array
#        assert self.action_space.contains(action)
#        demand = self.np_random.exponential(self.alpha)
#        lost_sales = -min(self.state[0] - demand, 0)
#        next_state = np.zeros(self.L + 1)
#        next_state[:-1], next_state[-1] = self.state[1:], action
#        next_state[0] = max(next_state[0] + self.state[0] - demand, 0)
#        self.state = next_state
#        self.steps = self.steps + 1
#        reward = -(self.h * self.state[0]  + self.p * lost_sales) / self.length
#        done = (self.steps >= self.length)
#        return self.state, reward, done, {}

#    def render(self, mode='ansi'):
#        outfile = sys.stdout if mode == 'ansi' else super(Inventory, self).render(mode=mode)
#        outfile.write(np.array2string(self.state))

#    def reset(self):
#        self.steps = 0 # keeps track of how many steps have been done in this episode
#        self.state = np.zeros(self.L + 1) # first entry is current inventory, remaining entries are outstanding orders
#        self.state[0] = self.start_inv # setting starting inventory
#        return self.state
    
    
    