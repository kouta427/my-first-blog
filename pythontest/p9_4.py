import matplotlib.pyplot as plt
steps = [8000, 6000, 4354, 7654, 6532, 3424, 3245] 
labels = ['C/C++', 'Python', 'Ruby', 'Java', 'PHP', 'C#', 'R']
num_bars = len(steps)
positions = range(1, num_bars+1)
plt.bar(labels, steps, align='center')
#plt.yticks(positions, labels)
plt.ylabel('Num')
plt.xlabel('Language')
plt.title('Population of programming language')
plt.grid()
plt.show()
