# importing mplot3d toolkits
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt

from typing import Tuple
from hyperopt import Trials

def get_coordinates(trials:Trials)->Tuple:
    """
    Get coordinates from hyperopt trials object

    :param trials: hyperopt trials object.
    :return: x, y, z coordinates.
    """    
    z = []
    x = []
    y = []
    for trial in trials.trials:
        print(trial)
        z.append(trial["result"]["loss"])
        x.append(trial["misc"]["vals"]["x"][0])
        y.append(trial["misc"]["vals"]["y"][0])
    
    return x, y, z

x, y, z = get_coordinates(trials)
# syntax for 3-D projection
ax = plt.axes(projection ='3d')
 
# defining axes
c = z
ax.scatter(x, y, z, c=c)

# syntax for plotting
ax.set_title('3d Scatter plot')
plt.show()
