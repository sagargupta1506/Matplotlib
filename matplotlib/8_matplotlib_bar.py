'''# Now in this section, we shall draw bar using bar()

import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3,8,1,10])

plt.bar(x,y)
plt.show()'''


# Now in this section, we shall draw Horizontal bar using bar()

'''import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3,8,1,10])

plt.barh(x,y)               # change only here
plt.show()'''



# Coloring of the bar() and barh() 
# https://matplotlib.org/stable/gallery/color/named_colors.html

'''import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3,8,1,10])

plt.bar(x,y, color="gray")               
plt.show()'''


# How we can change the bar width

import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3,8,1,10])

# plt.bar(x,y, width = 0.5)         # for vertically & default value is 0.5 or 1 
plt.barh(x,y, height = 0.3)         # for horizontally & default value is 0.8
plt.show()

