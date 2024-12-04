# Scatter: the scatter() function plots one dot for each observation.


'''import matplotlib.pyplot as plt
import numpy as np 

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

plt.scatter(x,y)
plt.show()'''



'''# Now we will compare 2 plots on the same figure
import matplotlib.pyplot as plt
import numpy as np 

# Day-1, the age and the speed of the cars:
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

plt.scatter(x,y)



# Day-2, the age and the speed of the cars:
x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y = np.array([100,105,84,105,90,99,95,94,100,79,112,91,89,80,85])

plt.scatter(x,y)

plt.show()'''


'''# Now we will set our own color
import matplotlib.pyplot as plt
import numpy as np 

# Day-1, the age and the speed of the cars:
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

plt.scatter(x,y, color="green")



# Day-2, the age and the speed of the cars:
x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y = np.array([100,105,84,105,90,99,95,94,100,79,112,91,89,80,85])

plt.scatter(x,y, color="hotpink")

plt.show()'''



'''# Now you also change the color of each "Dot"

import matplotlib.pyplot as plt
import numpy as np 

# Day-1, the age and the speed of the cars:
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

colors = (["red", "green", "blue", "yellow", "pink", "black", "orange", "beige", "purple", "gray", "cyan", "magenta", "brown"])

plt.scatter(x,y, c = colors)


plt.show()'''



'''# Now we will create color array and specify a colormap in scatter plot   (learn more about colormap from internet, basically for the coloring)

import matplotlib.pyplot as plt
import numpy as np 

# Day-1, the age and the speed of the cars:
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

colors = (["red", "green", "blue", "yellow", "pink", "black", "orange", "beign", "purple", "gray", "cyan", "magenta", "brown"])

colors = np.array([0,10,20,30,40,45,50,55,60,70,80,90,100])

plt.scatter(x,y, c = colors, cmap='viridis')
plt.colorbar()


plt.show()'''


'''# You can also change the size of the dots

import matplotlib.pyplot as plt
import numpy as np 

# Day-1, the age and the speed of the cars:
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

sizes = np.array([70,20,50,100,60,82,200,500,600,800,1000,300,150])

plt.scatter(x,y, s = sizes)


plt.show()'''



'''# alpha: you can adjust the transprancy of the dots and by default value is (1)

import matplotlib.pyplot as plt
import numpy as np 

# Day-1, the age and the speed of the cars:
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

sizes = np.array([70,20,50,100,60,82,200,500,600,800,1000,300,150])

plt.scatter(x,y, s = sizes, alpha = 0.5)    # changes only here

plt.show()'''


# Now we shall combine color, size, and alpha

import matplotlib.pyplot as plt
import numpy as np 

x = np.random.randint(100, size = (100))
y = np.random.randint(100, size = (100))
colors = np.random.randint(100, size = (100))
sizes = 10 *  np.random.randint(100, size = (100))

plt.scatter(x,y, c = colors, s = sizes, alpha = 0.5, cmap = 'nipy_spectral')

# 'nipy_spectral' is also a grident just like 'viridis'

plt.colorbar()
plt.show()



