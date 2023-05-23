import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()

# create a dot at the center
dot, = ax.plot([0], [0], 'o', color='black')

# create a sine wave for color shift
x = np.linspace(0, 2*np.pi, 100)
colors = np.sin(x)+1

# create a sine wave for alpha modulation
y = np.linspace(0, 1, 100)
alpha = np.sin(2*np.pi*y)+0.3
# adjust alpha modulation based on distance from center
alpha *= np.exp(-10*(x-np.pi)**2)

# define animation function
def animate(i):
    # update color and alpha of dot
    dot.set_color(plt.cm.cool(colors[i]))
    dot.set_alpha(alpha[i])
    return dot,

# set up animation
ani = FuncAnimation(fig, animate, frames=len(colors), 
                    interval=100, blit=True)

ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)

plt.show()
