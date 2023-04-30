import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
#
#x = [20, 40, 60, 80, 100, 110]
#y = [5, 10, 15, 20, 25, 30]
#
#fig = plt.figure()
#fig.patch.set_facecolor('black')
#
#ax = fig.add_subplot(111)
#ax.patch.set_facecolor('black')
#ax.tick_params(color='white', labelcolor='white')
#ax.spines['bottom'].set_color('white')
#ax.spines['top'].set_color('white')
#ax.spines['left'].set_color('white')
#ax.spines['right'].set_color('white')
#
#plt.grid(True, color='white', linestyle='dashed')
#plt.plot(x, y, color='lightblue', linewidth=2)
#plt.show()
#
fig, ax = plt.subplots()

# Set the size of the blip and the frequency of the pulsation
size = 0.3
freq = 2.0

# Define the x and y coordinates of the blip
x = 0.5
y = 0.5

# Define the number of frames for the animation
num_frames = 100

# Define the array of time values for the animation
t = np.linspace(0, 2*np.pi, num_frames)

# Define the array of alpha values for the animation
alpha_array = np.abs(np.sin(freq*t))

# Create the blip as a scatter plot
blip = ax.scatter(x, y, s=100, c='lightblue', marker='o', alpha=alpha_array[0])

# Define the update function for the animation
def update(frame):
    # Update the alpha value of the blip
    blip.set_alpha(alpha_array[frame])

# Create the animation
anim = animation.FuncAnimation(fig, update, frames=num_frames, interval=50)

# Set the limits of the plot
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)

# Display the animation
plt.show()
