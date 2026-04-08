import matplotlib.pyplot as plt
import numpy as np

# Data
foods = ["Meat", "Banana", "Avocados", "Sweet Potatoes", "Spinach", "Watermelon",
         "Coconut Water", "Beans", "Legumes", "Tomato"]

calories = [250, 130, 140, 120, 20, 20, 10, 50, 40, 19]
potassium = [40, 55, 20, 30, 40, 32, 10, 26, 25, 20]
fat = [8, 5, 3, 6, 1, 1.5, 0, 2, 1.5, 2.5]

x = np.arange(len(foods))  # X-axis positions
width = 0.25  # Width of the bars

# Plotting
plt.figure(figsize=(14, 6))
plt.bar(x - width, calories, width=width, label='Calories', color='salmon')
plt.bar(x, potassium, width=width, label='Potassium', color='gold')
plt.bar(x + width, fat, width=width, label='Fat', color='lightgreen')

plt.xlabel('Food Items')
plt.ylabel('Nutritional Values')
plt.title('Nutrition Chart: Calories, Potassium, and Fat')
plt.xticks(x, foods, rotation=45)
plt.legend()
plt.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.5)

plt.show()
