import numpy as np
import matplotlib.pyplot as plt

# Define the transformations (affine maps) for the Sierpiński Triangle
transformations = [
    lambda x, y: (0.5 * x, 0.5 * y),  # Bottom-left transformation
    lambda x, y: (0.5 * x + 0.5, 0.5 * y),  # Bottom-right transformation
    lambda x, y: (0.5 * x + 0.25, 0.5 * y + 0.5)  # Top transformation
]

def escape_time(x, y, max_iter=50):
    """
    Determines the escape time for a point (x, y).
    The escape condition is based on how close it remains to the transformations.
    """
    for i in range(max_iter):
        prev_x, prev_y = x, y
        x, y = transformations[np.random.randint(0, 3)](x, y)
        if abs(x - prev_x) < 1e-5 and abs(y - prev_y) < 1e-5:
            return i
    return max_iter  # If max iterations reached, assign max color

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
plt.title("Escape Time Algorithm - Sierpiński Triangle")
plt.show()