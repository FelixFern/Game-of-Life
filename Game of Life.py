import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
from matplotlib.colors import ListedColormap

n_generate = 500
a = np.zeros((100,100))
for i in range(n_generate):
    random_x = np.random.randint(0, len(a))
    random_y = np.random.randint(0, len(a))
    while a[random_y][random_x] == 1:
        random_x = np.random.randint(0, len(a))
        random_y = np.random.randint(0, len(a))
    a[random_y][random_x] = 1
print(a)

def generate_data():
    steps = [[-1, -1], [-1, 0], [-1, 1], [0, 1], [0, -1], [1, -1], [1, 0], [1, 1]]
    saved_a = a
    for i in range(len(a)):
        for j in range(len(a)):
            count = 0
            for step in steps:
                if -1 < i + step[0] < len(a) and -1 < j + step[1] < len(a):
                    if saved_a[j + step[1]][i + step[0]] == 1:
                        count += 1
            if saved_a[j][i] == 0: 
                if count >= 3:
                    a[j][i] = 1
            elif saved_a[j][i] == 1:
                if count <= 1 or count >= 4: 
                    a[j][i] = 0
    return a

def update(data):
    mat.set_data(data)
    return mat 

def data_gen():
    while True:
        yield generate_data()

cmap = ListedColormap(['w', 'r'])

fig, ax = plt.subplots()
mat = ax.matshow(generate_data(), cmap=cmap)
ani = animation.FuncAnimation(fig, update, data_gen, interval=100, save_count=50)
plt.show()