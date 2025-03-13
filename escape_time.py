import numpy as np
import matplotlib.pyplot as plt

numits = 20 
a = 0
b = 0
c = 1
d = 1
M = 100 
R = 200 

for p in range(1,M+1):
    for q in range(1,M+1):
        x = a + (c-a)*p/M
        y = b + (d-b)*p/M
        for n in range(1,numits+1):
            if y > 0.5:
                x = 2*x
                y = 2*y-1
            elif x > 0.5: 
                x = 2*x-1
                y = 2*y
            else:
                x = 2*x
                y = 2*y
            
            if x*x + y*y > R:
                plt.plot(x,y)


# Define image resolution
width, height = 500, 500
x_min, x_max = -0.1, 1.1
y_min, y_max = -0.1, 1.1

# Create escape time grid
image = np.zeros((height, width))

for i in range(width):
    for j in range(height):
        x = x_min + (x_max - x_min) * i / width
        y = y_min + (y_max - y_min) * j / height
        image[j, i] = escape_time(x, y)

# Plot the escape time fractal
plt.imshow(image, cmap="inferno", extent=[x_min, x_max, y_min, y_max])
plt.colorbar(label="Escape Time")
plt.title("Escape Time Algorithm - Sierpinski Triangle")
plt.show()