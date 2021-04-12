gym-inventory is a gym environment for inventory control with lost sales and positive lead times. 

The information below is mostly taken from the latex write-up, where additional details can be located. 


## State Space

The state of the system consists of two components: I_t, representing the current inventory level, and x_t = (x_{1,t}, ... , x_{L,t}), a vector of inventory orders that will arrive in the future (often referred to as a pipeline vector) [1]. We only require that these quantities be non-negative, and thus, the state space is S = { (I_t, x_t) : I_t, x_{1,t}, ... , x_{L,t} >= 0} [1]. For initial conditions, as in Xin & Goldberg (2016), we assume I_1 = 0 and x_{i,1} = 0 for i = 1, ..., L.


## Action Space

At each time t, a new inventory order must be placed. Since any non-negative order is a valid possible action, our action space is A = [0, infinity)  [1]. 


## Transitions

The description of the MDP follows that in [1]. At each time t, first the order x_{1,t} is delivered and added to the on-hand inventory. Then, a random amount of demand occurs (which is exponentially distributed with lambda = 1), and the amount of post-demand on-hand inventory is calculated. Costs are incurred if there are lost sales or remaining inventory on-hand. Finally, the pipeline vector is updated to account for the new order being placed (which is determined by some policy) and the other orders are shifted such that they are a day closer to being delivered. 


## Costs

At the end of each time period, penalties occur if there is leftover inventory or lost sales. A penalty h > 0 is incurred per unit of inventory on hand at the end of a time period, and a penalty p > 0 is incurred per lost unit of sales [1].


## Sources

[1] Xin, Linwei  Goldberg, David.  (2016).  Optimality Gap of Constant-Order Policies Decays Exponentially in theLead Time for Lost Sales Models.  Operations Research.  64.  10.1287/opre.2016.1514.

