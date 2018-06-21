import matplotlib.pyplot as plt
steps = [6543, 7000, 8900, 10789, 3467, 11045, 5095]
labels = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
num_bars = len(steps)
positions = range(1, num_bars+1)
plt.bar(labels, steps, align='center')
#plt.yticks(positions, labels)
plt.ylabel('Steps')
plt.xlabel('Day')
plt.title('Number of steps walked')
plt.grid()
plt.show()
