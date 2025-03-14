from PIL import Image
import colorsys
import math

#frame parameters
width = 500 #pixels
x_0 = -0.5
y_0 = 0
xRange = 2
aspectRatio = 1/1 
R = 2 #escape radius

precision = 70

height = round(width / aspectRatio)
yRange = xRange / aspectRatio
minX = x_0 - xRange / 2
maxX = x_0 + xRange / 2
minY = y_0 - yRange / 2
maxY = y_0 + yRange / 2

img = Image.new('RGB', (width, height), color = 'black')
pixels = img.load()

def simpleColor(distance):
    rgb = colorsys.hsv_to_rgb(distance,1,1)
    return tuple(round(i * 255) for i in rgb)

def logColor(distance, base, const, scale):
    color = -1 * math.log(distance, base)
    rgb = colorsys.hsv_to_rgb(const + scale * color,0.8,0.9)
    return tuple(round(i * 255) for i in rgb)

def sierpinski(x,y):
    if y > 0.5:
        x = 2*x
        y = 2*y - 1
    elif x > 0.5:
        x = 2*x - 1
        y = 2*y
    else:
        x = 2*x
        y = 2*y
    return x,y

def mandelbrot(x,y,oldX,oldY):
    a = x*x - y*y #real component of z^2
    b = 2 * x * y #imaginary component of z^2
    x = a + oldX #real component of new z
    y = b + oldY #imaginary component of new z
    return x,y

def julia(x,y):
    a = x*x - y*y #real component of z^2
    b = 2 * x * y #imaginary component of z^2
    x = a + x #real component of new z
    y = b + y #imaginary component of new z
    return x,y    

for row in range(height):
    for col in range(width):
        x = minX + col * xRange / width
        y = maxY - row * yRange / height
        #oldX = x    #oldX y oldY se usan para mandelbrot
        #oldY = y

        for i in range(precision + 1):
            #x,y = mandelbrot(x,y,oldX,oldY)
            #x,y = sierpinski(x,y)
            x,y = julia(x,y)
            if (x-x_0)**2 + (y-y_0)**2 > R**2:
                break

        if i < precision:
            distance = (i + 1) / (precision + 1)
            rgb = logColor(distance, 0.2, 0.27, 1.0)
            #rgb = simpleColor(distance)
            pixels[col,row] = rgb

img.show()