import numpy as np
import matplotlib.pyplot as plt

# data
mean = 5
std_dev = 2
values = np.random.normal(mean, std_dev, 1000)

# function h(x) = x^2 on [0,10]
x = np.linspace(0, 10, 100)
y = x**2

# plot (same axes)
plt.figure(figsize=(10, 6))
plt.hist(values, bins=30, alpha=0.6, label='Normal Distribution', edgecolor='black')
plt.plot(x, y, linewidth=2, label='h(x) = x²')

plt.xlabel('X axis'); plt.ylabel('Y axis')
plt.title('Histogram of Normal Distribution & Function h(x) = x²')
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()

# save PNG next to this script
plt.savefig('plot.png', dpi=300)
plt.show()