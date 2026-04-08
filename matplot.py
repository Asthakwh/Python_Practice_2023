#import matplotlib.pyplot as plt
#labels = ['section 1', 'section 2', 'section 3' ]
#sizes = [15, 30, 45]
#plt.show()
import matplotlib.pyplot as plt

labels = ['Section 1', 'Section 2', 'Section 3']
sizes = [15, 30, 45]

plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
plt.title("Simple Pie Chart")
plt.axis('equal')  # Ensures the pie is circular

plt.show()
