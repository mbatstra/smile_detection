import yfinance as yf
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt

# loading the data
indices = ["^GSPC","TLT", ]
data = yf.download(indices,start='2020-01-01')
data = data['Adj Close']
inv_growth = (data.pct_change().dropna() + 1).cumprod()

# plotting the data

fig, ax = plt.subplots()

ax.set_xlim(inv_growth.index[0], inv_growth.index[-1])
ax.set_ylim(0.940, 1.100)

line1, = ax.plot([], [])
line2, = ax.plot([], [])


def animation_frame(i):
    temp = inv_growth.iloc[:i]
    line1.set_data(temp.index, temp[0])
    line2.set_data(temp.index, temp[1])

    return line1,line2,

animation = FuncAnimation(fig, 
                          func=animation_frame, 
                          frames=range(inv_growth.index.size),
                          interval = 100)
plt.show()
