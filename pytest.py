import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

# Define the function to plot
def plot_graph():
    x = [20, 40, 60, 80, 100, 110]
    y = [5, 10, 15, 20, 25, 30]

    y = np.random.rand(100)
    x = np.arange(100)

    fig = plt.figure()
    fig.patch.set_facecolor('black')

    ax = fig.add_subplot(111)
    ax.patch.set_facecolor('black')
    ax.tick_params(color='white', labelcolor='white')
    ax.spines['bottom'].set_color('white')
    ax.spines['top'].set_color('white')
    ax.spines['left'].set_color('white')
    ax.spines['right'].set_color('white')

    plt.grid(True, color='white', linestyle='dashed')
    line, = plt.plot(x, y, color='lightblue', linewidth=2)

    # Set the size of the blip and the frequency of the pulsation
    size = 0.3
    freq = 2.0

    # Define the number of frames for the animation
    num_frames = 100

    # Define the array of time values for the animation
    t = np.linspace(0, 2*np.pi, num_frames)

    # Define the array of alpha values for the animation
    alpha_array = np.abs(np.sin(freq*t))

    # Create the blip as a scatter plot
    blip, = ax.plot(x[-1], y[-1], 'o', markersize=8, color='lightblue', alpha=alpha_array[0])

    # Define the update function for the animation
    def update(frame):
        # Update the alpha value of the blip
        blip.set_alpha(alpha_array[frame])
        # Update the position of the blip to the right-hand end of the line
        blip.set_data([x[-1]], [y[-1]])

    # Create the animation
    anim = animation.FuncAnimation(fig, update, frames=num_frames, interval=50)

    plt.show()

plot_graph()

