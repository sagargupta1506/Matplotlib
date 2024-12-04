# Display the multiple plots :- with subplot() you can draw multiple plots in one figure

'''import matplotlib.pyplot as plt
import numpy as np

# plot1
x = np.array([0,1,2,3])
y = np.array([3,8,1,10])

plt.subplot(1, 2, 1)      # The figure has 1 for 1_row, 2 for 2_column, and this is the 1 plot

plt.plot(x,y)

# plot2

x = np.array([0,1,2,3])
y = np.array([10,20,30,40])

plt.subplot(1,2,2)
plt.plot(x,y)


plt.show()'''


# Now we shall draw 2 plot on top of each other

'''import matplotlib.pyplot as plt
import numpy as np

# plot1
x = np.array([0,1,2,3])
y = np.array([3,8,1,10])

plt.subplot(2, 1, 1)        # changes only here

plt.plot(x,y)

# plot2

x = np.array([0,1,2,3])
y = np.array([10,20,30,40])

plt.subplot(2,1,2)                  # changes only here
plt.plot(x,y)


plt.show()'''


# Now we shall draw the challenge of 6 plot

import matplotlib.pyplot as plt
import numpy as np

# plot1
x = np.array([0,1,2,3])
y = np.array([3,8,1,10])

plt.subplot(2, 3, 1)               #(row,column,chart_no)  
plt.plot(x,y)
plt.title("Sales-2010")


# plot2
x = np.array([0,1,2,3])
y = np.array([10,20,30,40])

plt.subplot(2,3,2)                   #changes only here
plt.plot(x,y)
plt.title("Sales-2012")


# plot3
x = np.array([0,1,2,3])
y = np.array([3,8,5,10])

plt.subplot(2, 3, 3)                #changes only here  
plt.plot(x,y)
plt.title("Sales-2014")


# plot4
x = np.array([0,1,2,3])
y = np.array([10,20,30,40])

plt.subplot(2,3,4)                   #changes only here
plt.plot(x,y)
plt.title("Sales-2016")


# plot5
x = np.array([0,1,2,3])
y = np.array([3,8,1,10])

plt.subplot(2, 3, 5)                #changes only here  
plt.plot(x,y)
plt.title("Sales-2018")


# plot6
x = np.array([0,1,2,3])
y = np.array([10,20,30,60])

plt.subplot(2,3,6)                       #changes only here
plt.plot(x,y)
plt.title("Sales-2020")



plt.suptitle("My Shop")     # This is super title

plt.show()