import matplotlib.pyplot as plt

# Data
categories = ['A', 'B', 'C', 'D']
values = [15, 20, 10, 25]

# Create bar chart
plt.bar(categories, values, color=['red', 'green', 'blue', 'purple'])

# Customize
plt.title("Bar Chart Example")
plt.xlabel("Categories")
plt.ylabel("Values")

plt.show()