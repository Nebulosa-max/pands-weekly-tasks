import numpy as np
import matplotlib.pyplot as plt

# Generate 1000 values from a normal distribution
mean = 5
std_dev = 2
values = np.random.normal(mean, std_dev, 1000)

# Create x values for h(x) = x^2
x = np.linspace(0, 10, 100)
y = x ** 2

# Create the plot
plt.hist(values, bins=30, alpha=0.5, label='Normal Distribution')
plt.plot(x, y, color='red', label='h(x) = x²')

# Add labels and legend
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('Histogram & Function Plot')
plt.legend()

# Save the figure
plt.savefig('plot.png')

# Show the plot
plt.show()
