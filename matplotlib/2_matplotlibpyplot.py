'''
import matplotlib.pyplot as plt         # now the pyplot package can be reffered as plt

import numpy as np

# plotting x and y
# plot() : used to draw points/markers in a diagram, draw a line from one point to another point

# There are 2 parameters for specifying points in the diagram ie. x-axis and y-axis.

xpoints = np.array([1, 8])
ypoints = np.array([3, 10])

plt.plot(xpoints, ypoints)
plt.show()
'''

'''# plotting without line
import matplotlib.pyplot as plt
import numpy as np


xpoints = np.array([1,8])
ypoints = np.array([3,10])

plt.plot(xpoints, ypoints, 'o')
plt.show()'''


'''import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1,2,6,8])
ypoints = np.array([3,8,1,10])
plt.plot(xpoints, ypoints)
plt.show()'''


# Default X-Points :-  
# If we do not specify the points in x-axis then the default values 0,1,2,3,4,5.....will apply.
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3,8,1,10,5,7])
plt.plot(ypoints)
plt.show()







