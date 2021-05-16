# About Code
-------------
### Dependencies
Python 3.x, pytorch, numpy, matplotlib, stable_baselines3

### Installation
Simply clone the repo

### Summary of Files

inventory: contains the files for the implementation of our problem in an OpenAI Gym environment, as described above.

testing_policies: initial verification of our OpenAI Gym environment by testing several simple policies. (These results also provide validation for our method of estimating the long-run average cost.)

PPO_training_and_evaluation: performs PPO training on all problems using our original methodology. Additionally performs PPO training using modified parameters for large L and large p on the test case (p,L) = (99, 70). Once the best policies are obtained, this file also evaluates their performances and saves the results as a pickle object.

PPO_policy_plotting: creates plots of the training performance using info from the logs files. Additionally, for the L=1 case, creates visualizations of the trained policy.

create_tables: creates tables (comparable to table A.1. in Xin & Goldberg (2016)) that appear in the final write-up

Results:

---logs: contains logs of all our PPO training evaluations. Tracks the policy performance throughout the training process for each problem,      and additionally saves a copy of  the best model that was found throughout training. (The subfiles "logs" and "logs2" each contain a run      using our initial methodology, while the subfile "logs_largeL"      contains a run of our updated methodology for the (p,L) = (99, 70) test      case.) 

---objs: contains the pickle objects with the performance evaluation results of each policy. (The subfiles "objs" and "objs2" each contain a    run using our initial methodology)

# About Problem
------------------

Additional details can be located in the LaTeX document. 

### Problem Description

Inventory management is an important problem that many business must consider. The inventory management model we present here is one with lost sales and positive lead times. Lost sales means that any demand that isn't immediately fulfilled disappears and cannot be met in the future [2]. Positive lead times means that after more inventory is ordered, there is a delay (of L time steps) before it arrives [2].  Both of these assumptions match real life conditions for certain types of businesses: for instance, having lost sales is reasonable when competing business(es) exist [2]. 

### State Space

The state of the system consists of two components: I_t, the current amount of inventory held by the business, and x_t = (x_{1,t}, ... , x_{L,t}), which contains inventory orders that will arrive in the future, where L (a positive integer) is the lead time [2]. We assume that all these components are non-negative, so the state space is S = { (I_t, x_t) : I_t, x_{1,t}, ... , x_{L,t} >= 0} [2]. To match Xin & Goldberg (2016), we use I_1 = 0 and x_1 = (0, ..., 0) as initial conditions. 


### Action Space

At each time t, a new inventory order must be placed. The amount ordered is determined by the policy pi [2]. The action space is A = [0, infinity), since it it possible to place any non-negative inventory order [2]. 


### Transitions

The description of the MDP follows that in [2]. At each time t, first the order x_{1,t} is delivered and added to the on-hand inventory. Then, a random amount of demand occurs (which is exponentially distributed with lambda = 1), and the amount of post-demand on-hand inventory is calculated. Costs are incurred if there are lost sales or remaining inventory on-hand. Finally, the vector x_t is updated to account for the new order being placed (as determined by the policy pi), and the other orders are shifted such that they are a day closer to being delivered. 


### Costs

At the end of each time step, penalties occur in two situations: if there is leftover inventory (in which case the cost is h > 0 per unit of remaining inventory) or lost sales (in which case the cost is p > 0 per unit of unmet demand) [2]. We fix h = 1, but vary p throughout our implementation, as in [2]. The ultimate goal of this problem is to minimize the long-run average cost [2]. The long-run average cost was estimated in our simulations over a long time horizon (e.g., by truncating the infinite limit); tests were performed to ensure that this estimation method worked well for our purposes. 


### Constant Order Policy
A simple policy for this system is a constant-order policy, which always orders the same amount of inventory [2]. Xin & Goldberg (2016) proved that as the lead time increases, the gap between the performance of the optimal policy and the best constant-order policy converges to zero exponentially fast. Upper bounds for the ratio of the performance between the best constant-order policy and the optimal policy are given for various parameter combinations in Table A.1 from Xin & Goldberg (2016).

### Goal
Our goal is to train policies that achieve a smaller long-run average cost than the corresponding best constant-order policy, across a variety of combinations of p and L. We use PPO from the Stable Baselines3 package in Python to train our policies. We focus our attention on the situation when p is large (and notably when L is small), as this is the region of parameter space with the largest optimality bounds (and thus, the most potential room for improvement) [2]. 


### Sources

[1] Raffin, Antonin & Hill, Ashley & Ernestus, Maximilian & Gleave, Adam & Kanervisto, Anssi & Dormann, Noah. (2019). Stable Baselines3. GitHub, GitHub repository, https://github.com/DLR-RM/stable-baselines3

[2] Xin, Linwei & Goldberg, David.  (2016).  Optimality Gap of Constant-Order Policies Decays Exponentially in theLead Time for Lost Sales Models.  Operations Research.  64.  10.1287/opre.2016.1514.

