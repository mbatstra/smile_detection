from matplotlib.collections import LineCollection
from matplotlib.colors import ListedColormap, BoundaryNorm
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib as mpl
import numpy as np
import matplotlib.animation as animation
import opensimplex as simplex

simplex.seed(1234)
def simplex_wrap(i):
    return (simplex.noise2(x=i, y=0) + 1) / 2

x_global = np.arange(100)
y_global = np.array([simplex_wrap(i) for i in np.linspace(0, 2, 100)])
i_global = 2

def truncate_colormap(cmap, minval=0.0, maxval=1.0, n=100):
    new_cmap = colors.LinearSegmentedColormap.from_list(
        'trunc({n},{a:.2f},{b:.2f})'.format(n=cmap.name, a=minval, b=maxval),
        cmap(np.linspace(minval, maxval, n)))
    return new_cmap

def make_segments(x, y):
    '''
    Create list of line segments from x and y coordinates, in the correct format for LineCollection:
    an array of the form   numlines x (points per line) x 2 (x and y) array
    '''

    points = np.array([x, y]).T.reshape(-1, 1, 2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)
    
    return segments


# Interface to LineCollection:

def colorline(x, y, z=None, cmap=plt.get_cmap('copper'), norm=plt.Normalize(0.0, 1.0), linewidth=3, alpha=1.0):
    '''
    Plot a colored line with coordinates x and y
    Optionally specify colors in the array z
    Optionally specify a colormap, a norm function and a line width
    '''
    
    # Default colors equally spaced on [0,1]:
    if z is None:
        z = np.linspace(0.0, 1.0, len(x))
           
    # Special case if a single number:
    if not hasattr(z, "__iter__"):  # to check for numerical input -- this is a hack
        z = np.array([z])
        
    z = np.asarray(z)
    
    segments = make_segments(x, y)
    lc = LineCollection(segments, array=z, cmap=cmap, norm=norm, linewidth=linewidth, alpha=alpha)
    
    ax = plt.gca()
    ax.add_collection(lc)
    
    return lc

def update_values(y):
    global i_global
    i_global += 0.02
    y = np.append(y, simplex_wrap(i_global))
    y = np.delete(y, 0)
    return y

# Define the function to plot
def plot_graph():
    global x_global
    global y_global
    x = x_global
    y = y_global

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
    plt.ylim([0, 1])
    my_cmap = truncate_colormap(plt.get_cmap('cool'), 0.0, 0.5)
    line = colorline(x, y, cmap=my_cmap, linewidth=4)

    alpha_array = np.cos(np.linspace(0, np.pi * 0.5, 50))
    size_array = np.linspace(0, 50, 50)
    blip_outer, = ax.plot(x[-1], y[-1], 'o', markersize=0, color=my_cmap(0.99), alpha=alpha_array[0])
    blip_inner, = ax.plot(x[-1], y[-1], 'o', markersize=10, color=my_cmap(0.99), alpha=alpha_array[0])

    def blip_update(frame):
        #blip_inner.set_alpha(1)
        blip_outer.set_alpha(alpha_array[frame * 2 % 50])
        blip_outer.set_markersize(size_array[frame * 2 % 50])

    def line_update(frame):
        global y_global
        y_global = update_values(y_global)
        line.set_segments(make_segments(x_global, y_global))
        blip_outer.set_data([x[-1]], [y_global[-1]])
        blip_inner.set_data([x[-1]], [y_global[-1]])


    # Create the animation
    blip_anim = animation.FuncAnimation(fig, blip_update, frames=100, interval=50)
    line_anim = animation.FuncAnimation(fig, line_update, frames=100, interval=500)

    mng = plt.get_current_fig_manager()
    mng.full_screen_toggle()
    plt.show()

plot_graph()
