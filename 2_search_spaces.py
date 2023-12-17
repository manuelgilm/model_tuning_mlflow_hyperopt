import hyperopt
from hyperopt import hp
import numpy as np
 

# The stochastic expressions currently recognized by hyperopt's optimization algorithms are:

# space =  hp.choice(label = "options", options=["option1", "option2", hp.choice("option3", ["option3_1", "option3_2"])])  
# print(space)
# Returns one of the options, which should be a list or tuple. The elements of options can themselves
# be [nested] stochastic expressions.

# ----------------------------------------------------------------------------------------------------------------------------

# space = hp.randint(label="label" , low=5, high=10)

# Returns a random integer in the range  [low, high).
# This is an appropriate distribution for describing random seeds for example. 
# ----------------------------------------------------------------------------------------------------------------------------
# space = hp.uniform(label="label", low=1, high=7)

# Returns a value uniformly between low and high.

# ----------------------------------------------------------------------------------------------------------------------------
# space = hp.quniform(label = "label", low = 0, high=100, q=5)
# Returns a value like round(uniform(low, high) / q) * q

# ----------------------------------------------------------------------------------------------------------------------------
space = hp.loguniform(label="label", low=np.log(0.0001), high=np.log(1.0))
# lr = 0.0001, 0.001, 0.01, 0.1, 1.0
print(hyperopt.pyll.stochastic.sample(space))
# Returns a value drawn according to exp(uniform(low, high)) so that the logarithm of the return value is 
# uniformly distributed.



