import matplotlib.pyplot as plt


student = [1, 2, 3, 4, 5]

height = [156, 144, 173, 167, 131]

# labels for bars
tick_label = ['Arjun', 'Aadarsh', 'John', 'Steve', 'Rohit']

# plotting a bar chart
plt.bar(student, height, tick_label = tick_label,
        width = 0.8, color = ['red', 'blue', 'orange', 'purple', 'green'])

# naming the x-axis
plt.xlabel('Person Name')
# naming the y-axis
plt.ylabel('Heights Of People (in cm)')
# plot title
plt.title('Different Poeple And Their Heights')

# function to show te plot
plt.show()
