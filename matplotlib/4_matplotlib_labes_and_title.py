# Create labels for a plot
'''
import matplotlib.pyplot as plt
import numpy as np

x = np.array([80,85,90,95,100,105,110,115,120,125])
y = np.array([240,250,260,270,280,290,300,310,320,330])

plt.plot(x, y)

plt.title("Health Moniter")         # Giving the title in the Plot

plt.xlabel("Average oxygen")        # Giving the label in x-axis
plt.ylabel("Our calorie")           # Giving the label in y-axis

plt.show()
'''

# Now we shall set the font property for title and labels via a "fontdict"

'''
import matplotlib.pyplot as plt
import numpy as np

x = np.array([80,85,90,95,100,105,110,115,120,125])
y = np.array([240,250,260,270,280,290,300,310,320,330])


font1 = {'family':'serif','color':'blue','size':20}     # Dictonary
font2 = {'family':'serif', 'color':'darkred','size':15}

plt.plot(x, y)

plt.title("Health Moniter", fontdict=font1)         

plt.xlabel("Average oxygen", fontdict=font2)        
plt.ylabel("Our calorie", fontdict=font2)           

plt.show()
'''


# You can also change the location of the title via "loc"
# and default position is center

import matplotlib.pyplot as plt
import numpy as np

x = np.array([80,85,90,95,100,105,110,115,120,125])
y = np.array([240,250,260,270,280,290,300,310,320,330])


font1 = {'family':'serif','color':'blue','size':20}     # Dictonary
font2 = {'family':'serif', 'color':'darkred','size':15}

plt.plot(x, y)

plt.title("Health Moniter", fontdict=font1, loc='left')         

plt.xlabel("Average oxygen", fontdict=font2)        
plt.ylabel("Our calorie", fontdict=font2)           

plt.show()




