# Problem Set-up

The following is mostly taken from the latex write-up, where additional details can be located. 

## Problem Description

Optimal inventory management is a major concern for many business.  Here,  we consider an inventory management problem that exhibits two key traits: positive lead times and lost sales. In a system with positive lead times, after an order for more inventory is placed, there is a delay before it is received [2].  This is a reasonable assumption because, in many real life situations, it takes a non-negligible amount of time for a product that is ordered to be produced and shipped to a business.  On the other hand, lost sales means that if there is more demand than there is inventory on hand, then any demand that is not fulfilled disappears and cannot be met at a later date [2]. In real life, this may occur when competing business(es) exist, as customers with unmet demand may simply take their business elsewhere [2].

## State Space

The state of the system consists of two components: I_t, representing the current inventory level, and x_t = (x_{1,t}, ... , x_{L,t}), a vector of inventory orders that will arrive in the future (often referred to as a pipeline vector), where L (a positive integer) is the lead time [2]. We only require that these quantities be non-negative, and thus, the state space is S = { (I_t, x_t) : I_t, x_{1,t}, ... , x_{L,t} >= 0} [2]. For initial conditions, as in Xin & Goldberg (2016), we assume I_1 = 0 and x_{i,1} = 0 for i = 1, ..., L.


## Action Space

At each time t, a new inventory order must be placed. Since any non-negative order is a valid possible action, our action space is A = [0, infinity)  [2]. 


## Transitions

The description of the MDP follows that in [2]. At each time t, first the order x_{1,t} is delivered and added to the on-hand inventory. Then, a random amount of demand occurs (which is exponentially distributed with lambda = 1), and the amount of post-demand on-hand inventory is calculated. Costs are incurred if there are lost sales or remaining inventory on-hand. Finally, the pipeline vector is updated to account for the new order being placed (which is determined by some policy) and the other orders are shifted such that they are a day closer to being delivered. 


## Costs

At the end of each time period, penalties occur if there is leftover inventory or lost sales. A penalty h > 0 is incurred per unit of inventory on hand at the end of a time period, and a penalty p > 0 is incurred per lost unit of sales [2]. The ultimate goal is to minimize the long run average cost.


## Constant Order Policy
A simple policy for this system is a constant-order policy, in which the same amount of inventory is always ordered (regardless  of  the  amount  of  inventory  on  hand,  the  amount  of  inventory  that  has  beenordered  but  has  not  yet  arrived,  etc.) [2]. Xin & Goldberg (2016) proved that as the lead time increases, the gap between the performance of the optimal policy and the best constant-order policy converges to zero exponentially fast. Upper bounds for the ratio of the performance between the best constant-order policy and the optimal policy are given for various parameter combinations in Table A.1 from Xin & Goldberg (2016).

## Goal
Our ultimate goal will be to,  in a wide parameter space,  train policies using deep RL algorithms that achieve better performance than the best constant-order policy. Specifically, we will use PPO from the Stable Baselines3 package in Python. We focus our attention on the situation when p is large (and notably when L is small), as this is the region of parameter space with the largest optimality bounds [1]. 


## Summary of Files

inventory: contains the files for the implementation of our problem in an OpenAI Gym environment, as described above.

testing_policies: initial verification of our OpenAI Gym environment by testing several simple policies

PPO_training_and_evaluation: performs PPO training on all problems using our original methodology. Additionally performs PPO training using modified parameters for large L and large p on the test case (p,L) = (99, 70). Once the best policies are obtained, this file also evaluates their performances and saves the results as a pickle object.

PPO_policy_plotting: creates plots of the training performance using info from the logs files. Additionally, for the L=1 case, creates visualizations of the trained policy.

create_tables: creates tables (comparable to table A.1. in Xin & Goldberg (2016)) that appear in the final write-up

Results:

---logs: contains logs of all our PPO training evaluations. Tracks the policy performing throughout the training process for each problem,      and additionally saves a copy of  the best model that was found throughout training. (The subfiles "logs" and "logs2" each contain a run      using our initial methodology, while the subfile "logs_largeL"      contains a run of our updated methodology for the (p,L) = (99, 70) test      case.) 

---objs: contains the pickle objects with the performance evaluation results of each policy. (The subfiles "objs" and "objs2" each contain a    run using our initial methodology)


## Sources

[1] Raffin, Antonin & Hill, Ashley & Ernestus, Maximilian & Gleave, Adam & Kanervisto, Anssi & Dormann, Noah. (2019). Stable Baselines3. GitHub, GitHub repository, https://github.com/DLR-RM/stable-baselines3

[2] Xin, Linwei & Goldberg, David.  (2016).  Optimality Gap of Constant-Order Policies Decays Exponentially in theLead Time for Lost Sales Models.  Operations Research.  64.  10.1287/opre.2016.1514.

