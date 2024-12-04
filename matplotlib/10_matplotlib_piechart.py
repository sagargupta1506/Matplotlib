# Creating the pie chart. using pie()

'''import matplotlib.pyplot as plt
import numpy as np

y = np.array([35,25,25,15])
plt.pie(y)
plt.show()'''

# Now will lable the pie chart

'''import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 29, 15])
mylables = ["Apple", "Banana", "Cherry", "Mango"]   #change

plt.pie(y, labels=mylables)
plt.show()'''

# startangle parameter : the default start angle is x axis but you can change the start angle by specifying startangle parameter
# and the default angle is 0

'''import matplotlib.pyplot as plt
import numpy as np

y = np.array([70, 20, 90, 50])
mylables = ["Apple", "Banana", "Cherry", "Mango"]

plt.pie(y, labels=mylables, startangle=90)  # some changes
plt.show()
'''


# How to explode the pie chart by a value

'''import matplotlib.pyplot as plt
import numpy as np

y = np.array([90, 90, 90, 90])
mylables = ["Apple", "Banana", "Cherry", "Mango"]
myexplode = [0.2, 0, 0, 0]      # these are wedge or say distance

plt.pie(y, labels=mylables, explode=myexplode, shadow=True)  # some changes
plt.show()'''


# You can also specify the color fo reach wedge:

'''import matplotlib.pyplot as plt
import numpy as np

y = np.array([70, 90, 40, 62])
mylables = ["Apple", "Banana", "Cherry", "Mango"]

mycolor = ["k", "hotpink", "b", "#4CAF50"]


plt.pie(y, labels=mylables,colors=mycolor)  # some changes
plt.show()'''



# We can also add the legend(list of explanation)

import matplotlib.pyplot as plt
import numpy as np

y = np.array([70, 90, 40, 62])
mylables = ["Apple", "Banana", "Cherry", "Mango"]


plt.pie(y, labels=mylables)

plt.legend(title="Fruits")            # legend() with header
plt.show()


 