# Histogram : it is a graph showing the frequency distribution.

# eg. say you ask for the height of the 250 people then how we will make a histogram

# by using hist()


'''import numpy as np
x = np.random.normal(170,10,250)

print(x)'''


#the hist() will read the array and produce the histogram

import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(170,10,250)

plt.hist(x)
plt.show()